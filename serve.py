#!/usr/bin/env python3
"""Umwelt dev server — like `python3 -m http.server 8770` but sends Cache-Control: no-store,
so the browser ALWAYS fetches the latest mix.html on a plain reload (no more stale pages)."""
import http.server, socketserver

PORT = 8770

class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, must-revalidate')
        self.send_header('Expires', '0')
        super().end_headers()

socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("", PORT), NoCacheHandler) as httpd:
    print(f"serving Umwelt on http://localhost:{PORT} (no-cache)")
    httpd.serve_forever()
