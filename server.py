"""Blossom Planner - server with static file support."""
import json
import os
import re
import sys
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from urllib.parse import urlparse, parse_qs

APP_DIR = Path(__file__).parent
DATA_DIR = APP_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

class BlossomHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path.rstrip("/")

        if path in ("", "/", "/index.html", "/blossom.html"):
            self.send_file(APP_DIR / "blossom.html", "text/html")
        elif path == "/blossom-dictionary.txt":
            self.send_file(APP_DIR / "blossom-dictionary.txt", "text/plain")
        elif path == "/app.js":
            self.send_file(APP_DIR / "app.js", "application/javascript")
        elif path == "/styles.css":
            self.send_file(APP_DIR / "styles.css", "text/css")
        else:
            self.send_error(404, "Not found")

    def send_json(self, data, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def send_file(self, path, content_type="application/octet-stream"):
        try:
            with open(path, "rb") as f:
                content = f.read()
            self.send_response(200)
            self.send_header("Content-Type", content_type)
            self.send_header("Cache-Control", "no-cache")
            self.end_headers()
            self.wfile.write(content)
        except FileNotFoundError:
            self.send_error(404, "File not found")

    def log_message(self, format, *args):
        pass

def main():
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 6142
    server = HTTPServer(("0.0.0.0", port), BlossomHandler)
    print(f"Blossom Planner running at http://localhost:{port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down...")
        server.server_close()

if __name__ == "__main__":
    main()
