#!/usr/bin/env python3
"""POST a sample payload to the mock server using only the Python standard library."""
import json
import os
import urllib.error
import urllib.request

URL = os.environ.get("MOCK_INFER_URL", "http://127.0.0.1:8080/infer")
API_KEY = os.environ.get("MOCK_INFER_API_KEY")

payload = {
    "photo_path": "/tmp/example.jpg",
    "metrics": {"sharpness": 42.0, "brightness": 120.0},
    "thresholds": {"min_sharpness": 20.0},
}

data = json.dumps(payload).encode("utf-8")
req = urllib.request.Request(URL, data=data, method="POST")
req.add_header("Content-Type", "application/json")
if API_KEY:
    req.add_header("Authorization", f"Bearer {API_KEY}")

try:
    with urllib.request.urlopen(req, timeout=5) as resp:
        body = json.loads(resp.read().decode("utf-8"))
        print(json.dumps(body, indent=2, ensure_ascii=False))
except urllib.error.HTTPError as e:
    print(f"HTTP {e.code}: {e.read().decode('utf-8', errors='replace')}")
except urllib.error.URLError as e:
    print(f"Connection failed ({e}). Is mock_server.py running?")
