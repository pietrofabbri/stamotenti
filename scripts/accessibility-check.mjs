#!/usr/bin/env node
// A4 (PHASE-2-PLAN.md) — controllo di accessibilità automatico.
//
// Cosa fa:
//   1. builda il sito Hugo (hugo build --gc --minify);
//   2. serve public/ localmente con un piccolo server statico;
//   3. apre ogni pagina reale generata in Chromium headless (Puppeteer);
//   4. inietta axe-core (locale, da node_modules, nessuna rete/CDN) ed
//      esegue axe.run() su ogni pagina;
//   5. stampa un report leggibile: violazioni per pagina, per severità.
//
// Le pagine sotto content/fixtures/ (IT ed EN) sono escluse dal report
// principale — non sono contenuto editoriale reale — ma vengono comunque
// controllate e riportate in una sezione separata, perché sono comunque
// codice reale (layouts/shortcodes/figure.html, layouts/partials/seo.html,
// ecc.) che vale la pena verificare.
//
// Come rieseguirlo:
//   npm install        # una tantum, installa axe-core + puppeteer
//   npx puppeteer browsers install chrome   # una tantum, scarica Chromium
//                                            # (~830MB in ~/.cache/puppeteer,
//                                            # fuori dal repository)
//   npm run a11y       # oppure: node scripts/accessibility-check.mjs
//
// Non è collegato a CI ed esegue solo in locale, per decisione esplicita
// del proprietario (A4, PHASE-2-PLAN.md, 2026-08-18) — nessun servizio
// esterno è coinvolto: axe-core e Chromium sono entrambi locali.
//
// Exit code: 0 se nessuna violazione impact=serious|critical sulle pagine
// reali; 1 altrimenti. Le violazioni sulle pagine fixture non influenzano
// l'exit code (sono un controllo informativo separato).

import { createServer } from "node:http";
import { readFile, readdir, stat } from "node:fs/promises";
import { existsSync } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { execFileSync } from "node:child_process";
import puppeteer from "puppeteer";

const ROOT = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const PUBLIC_DIR = path.join(ROOT, "public");
const AXE_SOURCE_PATH = path.join(ROOT, "node_modules", "axe-core", "axe.min.js");

const CONTENT_TYPES = {
  ".html": "text/html; charset=utf-8",
  ".css": "text/css; charset=utf-8",
  ".js": "text/javascript; charset=utf-8",
  ".mjs": "text/javascript; charset=utf-8",
  ".xml": "application/xml; charset=utf-8",
  ".txt": "text/plain; charset=utf-8",
  ".svg": "image/svg+xml",
  ".png": "image/png",
  ".jpg": "image/jpeg",
  ".webp": "image/webp",
  ".ico": "image/x-icon",
  ".json": "application/json; charset=utf-8",
};

function log(line = "") {
  process.stdout.write(line + "\n");
}

function buildSite() {
  log("== Build Hugo ==");
  execFileSync("hugo", ["build", "--gc", "--minify"], {
    cwd: ROOT,
    stdio: "inherit",
  });
}

const META_REFRESH_RE = /<meta\s+http-equiv=["']?refresh["']?/i;

async function findHtmlPages(dir, base = dir) {
  const entries = await readdir(dir, { withFileTypes: true });
  let pages = [];
  for (const entry of entries) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      pages = pages.concat(await findHtmlPages(full, base));
    } else if (entry.isFile() && entry.name === "index.html") {
      const rel = path.relative(base, path.dirname(full));
      const urlPath = "/" + (rel === "" ? "" : rel.replace(/\\/g, "/") + "/");
      const content = await readFile(full, "utf8");
      const isRedirectAlias = META_REFRESH_RE.test(content);
      pages.push({ urlPath, isRedirectAlias });
    }
  }
  return pages;
}

function startServer(rootDir) {
  return new Promise((resolve) => {
    const server = createServer(async (req, res) => {
      try {
        const decoded = decodeURIComponent(req.url.split("?")[0]);
        let filePath = path.join(rootDir, decoded);
        if (!filePath.startsWith(rootDir)) {
          res.writeHead(403);
          res.end();
          return;
        }
        if (existsSync(filePath) && (await stat(filePath)).isDirectory()) {
          filePath = path.join(filePath, "index.html");
        }
        if (!existsSync(filePath)) {
          res.writeHead(404);
          res.end("Not found");
          return;
        }
        const ext = path.extname(filePath);
        const body = await readFile(filePath);
        res.writeHead(200, {
          "Content-Type": CONTENT_TYPES[ext] || "application/octet-stream",
        });
        res.end(body);
      } catch (err) {
        res.writeHead(500);
        res.end(String(err));
      }
    });
    server.listen(0, "127.0.0.1", () => resolve(server));
  });
}

function isFixturePage(urlPath) {
  return urlPath.includes("/fixtures/");
}

const IMPACT_ORDER = { critical: 0, serious: 1, moderate: 2, minor: 3 };

function sortByImpact(violations) {
  return [...violations].sort(
    (a, b) => (IMPACT_ORDER[a.impact] ?? 9) - (IMPACT_ORDER[b.impact] ?? 9)
  );
}

async function checkPage(browser, baseUrl, urlPath, axeSource) {
  const page = await browser.newPage();
  const localOrigin = new URL(baseUrl).origin;
  // Sicurezza: strumento dichiaratamente "solo locale" (A4, PHASE-2-PLAN.md) —
  // nessuna richiesta deve mai uscire verso una rete esterna, anche se il
  // markup buildato contiene un URL assoluto reale (es. una pagina di alias
  // con <meta http-equiv=refresh> verso https://stamotenti.it/, generata
  // automaticamente da Hugo). Trovato durante la prima esecuzione di questo
  // script: senza questo blocco, controllare /it/ tentava una navigazione
  // reale verso il dominio di produzione.
  await page.setRequestInterception(true);
  page.on("request", (req) => {
    const reqUrl = new URL(req.url());
    if (reqUrl.origin === localOrigin || reqUrl.protocol === "data:") {
      req.continue();
    } else {
      req.abort();
    }
  });
  try {
    await page.goto(baseUrl + urlPath, { waitUntil: "networkidle0" });
    await page.evaluate(axeSource);
    const results = await page.evaluate(async () => {
      // eslint-disable-next-line no-undef
      return await axe.run(document, {
        runOnly: { type: "tag", values: ["wcag2a", "wcag2aa", "wcag21a", "wcag21aa"] },
      });
    });
    return results.violations;
  } finally {
    await page.close();
  }
}

function printPageReport(urlPath, violations) {
  if (violations.length === 0) {
    log(`  OK    ${urlPath}`);
    return;
  }
  log(`  FAIL  ${urlPath}  (${violations.length} regola/e violata/e)`);
  for (const v of sortByImpact(violations)) {
    log(`          [${v.impact ?? "?"}] ${v.id} — ${v.help}`);
    log(`            ${v.helpUrl}`);
    log(`            nodi coinvolti: ${v.nodes.length}`);
    for (const node of v.nodes.slice(0, 3)) {
      log(`              - ${node.target.join(" ")}`);
    }
    if (v.nodes.length > 3) {
      log(`              ... e altri ${v.nodes.length - 3}`);
    }
  }
}

function summarize(label, allViolations) {
  const counts = { critical: 0, serious: 0, moderate: 0, minor: 0 };
  let pagesWithViolations = 0;
  for (const violations of Object.values(allViolations)) {
    if (violations.length > 0) pagesWithViolations++;
    for (const v of violations) {
      counts[v.impact] = (counts[v.impact] ?? 0) + 1;
    }
  }
  const totalPages = Object.keys(allViolations).length;
  log(
    `${label}: ${totalPages} pagine controllate, ${pagesWithViolations} con violazioni. ` +
      `critical=${counts.critical} serious=${counts.serious} moderate=${counts.moderate} minor=${counts.minor}`
  );
  return counts;
}

async function main() {
  if (!existsSync(AXE_SOURCE_PATH)) {
    log("ERRORE: node_modules/axe-core non trovato. Esegui prima: npm install");
    process.exit(2);
  }

  buildSite();

  if (!existsSync(PUBLIC_DIR)) {
    log("ERRORE: public/ non trovato dopo la build.");
    process.exit(2);
  }

  const allPages = (await findHtmlPages(PUBLIC_DIR)).sort((a, b) =>
    a.urlPath.localeCompare(b.urlPath)
  );
  const redirectPages = allPages.filter((p) => p.isRedirectAlias);
  const checkablePages = allPages.filter((p) => !p.isRedirectAlias);
  const realPages = checkablePages.filter((p) => !isFixturePage(p.urlPath));
  const fixturePages = checkablePages.filter((p) => isFixturePage(p.urlPath));

  log(
    `\nPagine trovate: ${allPages.length} totali (${realPages.length} reali, ` +
      `${fixturePages.length} fixture, ${redirectPages.length} alias di redirect tecnico esclusi)\n`
  );
  if (redirectPages.length > 0) {
    for (const p of redirectPages) {
      log(`  SKIP (redirect tecnico, non contenuto): ${p.urlPath}`);
    }
    log("");
  }

  const server = await startServer(PUBLIC_DIR);
  const { port } = server.address();
  const baseUrl = `http://127.0.0.1:${port}`;

  const axeSource = await readFile(AXE_SOURCE_PATH, "utf8");

  const browser = await puppeteer.launch({ headless: true });

  const realResults = {};
  const fixtureResults = {};

  try {
    log("== Pagine reali ==");
    for (const { urlPath } of realPages) {
      const violations = await checkPage(browser, baseUrl, urlPath, axeSource);
      realResults[urlPath] = violations;
      printPageReport(urlPath, violations);
    }

    log("\n== Pagine fixture (content/fixtures/) — verifica separata, informativa ==");
    for (const { urlPath } of fixturePages) {
      const violations = await checkPage(browser, baseUrl, urlPath, axeSource);
      fixtureResults[urlPath] = violations;
      printPageReport(urlPath, violations);
    }
  } finally {
    await browser.close();
    server.close();
  }

  log("\n== Riepilogo ==");
  const realCounts = summarize("Pagine reali", realResults);
  summarize("Pagine fixture", fixtureResults);

  const blocking = realCounts.critical + realCounts.serious;
  if (blocking > 0) {
    log(`\nRISULTATO: violazioni critical/serious trovate su pagine reali (${blocking}). Vedi dettagli sopra.`);
    process.exitCode = 1;
  } else {
    log("\nRISULTATO: nessuna violazione critical/serious sulle pagine reali.");
    process.exitCode = 0;
  }
}

main().catch((err) => {
  console.error(err);
  process.exit(2);
});
