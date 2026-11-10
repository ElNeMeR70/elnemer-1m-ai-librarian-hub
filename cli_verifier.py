#!/usr/bin/env python3
"""
ElNemer 1-Million AI Books & Semantic Knowledge Graph — Self-Hosted Research Librarian Hub — Command-Line Verification & Metadata Client
Author: Eng. Mahmoud Bek ElNemer (ORCID: 0009-0008-7553-2167)
License: MIT
"""
import sys, json, urllib.request

UPSTREAM = "https://million.elnemer-ai.com"

def inspect_volume(vol_id: int = 5000001):
    url = f"{UPSTREAM}/knowledge-graph?id={vol_id}&format=jsonld"
    req = urllib.request.Request(url, headers={"User-Agent": "ElNemer-CLI/1.0"})
    with urllib.request.urlopen(req, timeout=12) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    print(json.dumps(data, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    vid = int(sys.argv[1]) if len(sys.argv) > 1 else 5000001
    inspect_volume(vid)
