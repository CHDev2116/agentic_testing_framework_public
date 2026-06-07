#!/usr/bin/env python3
"""Validate mock /infer response against the public inference contract."""
from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request

URL = os.environ.get("MOCK_INFER_URL", "http://127.0.0.1:8080/infer")
API_KEY = os.environ.get("MOCK_INFER_API_KEY")

VALID_DECISIONS = frozenset(
    {"Optimal", "Blurry", "Under-exposed", "Over-exposed", "Error"}
)

PAYLOAD = {
    "photo_path": "/tmp/contract_smoke.jpg",
    "metrics": {"sharpness": 42.0, "brightness": 120.0},
    "thresholds": {"min_sharpness": 20.0},
}


def normalize_result(body: dict) -> dict:
    if "result" in body and isinstance(body["result"], dict):
        return body["result"]
    return body


def check_field(result: dict, name: str, expected_type: type) -> None:
    if name not in result:
        raise AssertionError(f"missing required field: {name}")
    if not isinstance(result[name], expected_type):
        raise AssertionError(
            f"{name} must be {expected_type.__name__}, got {type(result[name]).__name__}"
        )
    if expected_type is str and not result[name].strip():
        raise AssertionError(f"{name} must be non-empty")


def main() -> int:
    data = json.dumps(PAYLOAD).encode("utf-8")
    req = urllib.request.Request(URL, data=data, method="POST")
    req.add_header("Content-Type", "application/json")
    if API_KEY:
        req.add_header("Authorization", f"Bearer {API_KEY}")

    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            if resp.status != 200:
                print(f"FAIL: expected HTTP 200, got {resp.status}", file=sys.stderr)
                return 1
            body = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print(f"FAIL: HTTP {e.code}", file=sys.stderr)
        return 1
    except urllib.error.URLError as e:
        print(f"FAIL: connection error ({e})", file=sys.stderr)
        return 1
    except json.JSONDecodeError as e:
        print(f"FAIL: response is not JSON ({e})", file=sys.stderr)
        return 1

    result = normalize_result(body)
    try:
        check_field(result, "decision", str)
        check_field(result, "code", str)
        check_field(result, "msg", str)
        if result["decision"] not in VALID_DECISIONS:
            raise AssertionError(
                f"decision {result['decision']!r} not in {sorted(VALID_DECISIONS)}"
            )
    except AssertionError as e:
        print(f"FAIL: {e}", file=sys.stderr)
        return 1

    print(
        json.dumps(
            {
                "status": "ok",
                "decision": result["decision"],
                "code": result["code"],
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
