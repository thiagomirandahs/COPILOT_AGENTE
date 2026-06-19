// Adir Chat — servidor minimo (zero dependencias).
// Serve a interface e faz proxy pro Ollama (mesma origem = sem CORS).
const http = require("http");
const fs = require("fs");
const path = require("path");

const PORT = 3000;
const OLLAMA = { host: "127.0.0.1", port: 11434 };

const server = http.createServer((req, res) => {
  // 1) Servir a pagina
  if (req.method === "GET" && (req.url === "/" || req.url === "/index.html")) {
    fs.readFile(path.join(__dirname, "index.html"), (err, html) => {
      if (err) { res.writeHead(500); res.end("index.html nao encontrado"); return; }
      res.writeHead(200, { "Content-Type": "text/html; charset=utf-8" });
      res.end(html);
    });
    return;
  }

  // 2) Proxy de /api/* pro Ollama (chat, tags, etc.)
  if (req.url.startsWith("/api/")) {
    const proxyReq = http.request(
      { host: OLLAMA.host, port: OLLAMA.port, path: req.url, method: req.method,
        headers: { "Content-Type": "application/json" } },
      (proxyRes) => {
        res.writeHead(proxyRes.statusCode, proxyRes.headers);
        proxyRes.pipe(res);
      }
    );
    proxyReq.on("error", (e) => {
      res.writeHead(502, { "Content-Type": "application/json" });
      res.end(JSON.stringify({ error: "Ollama nao respondeu (ele esta rodando?): " + e.message }));
    });
    req.pipe(proxyReq);
    return;
  }

  res.writeHead(404); res.end("Not found");
});

server.listen(PORT, () => {
  console.log("\n  ✅ Adir Chat no ar:  http://localhost:" + PORT + "\n  (feche esta janela ou Ctrl+C para parar)\n");
});
