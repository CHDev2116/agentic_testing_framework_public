#!/usr/bin/env python3
"""Minimal mock inference server — same contract as the full framework's mock_api backend."""
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os

API_KEY = os.environ.get("MOCK_INFER_API_KEY")


class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path != "/infer":
            self.send_error(404)
            return
        length = int(self.headers.get("Content-Length", "0") or "0")
        raw = self.rfile.read(length).decode("utf-8") if length else "{}"
        try:
            body = json.loads(raw)
        except json.JSONDecodeError:
            self.send_response(400)
            self.end_headers()
            return

        auth = self.headers.get("Authorization", "")
        if API_KEY and auth != f"Bearer {API_KEY}":
            self.send_response(401)
            self.end_headers()
            return

        metrics = body.get("metrics") or {}
        sharp = float(
            metrics.get("sharpness", metrics.get("laplacian_variance", 50))
        )
        decision = "Optimal" if sharp >= 30 else "Blurry"
        result = {
            "decision": decision,
            "code": "SUCCESS_200",
            "msg": "mock_api_minimal stub classification",
        }
        payload = json.dumps({"result": result}).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def log_message(self, *_args):
        return


if __name__ == "__main__":
    print("Listening on http://127.0.0.1:8080/infer (POST JSON: photo_path, metrics, thresholds)")
    HTTPServer(("127.0.0.1", 8080), Handler).serve_forever()
