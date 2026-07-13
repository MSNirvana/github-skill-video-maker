#!/usr/bin/env python3
"""Block external-channel and third-party-action signals before delivery."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from platform_safety import dumps_result, scan_brief, scan_text


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate public-platform text for external-channel risk.")
    parser.add_argument("--brief", default="", help="Optional video brief JSON")
    parser.add_argument("--text", action="append", default=[], help="Narration, SRT, publishing pack, TSX, or other public text file; repeat as needed")
    args = parser.parse_args()

    findings: list[dict[str, str]] = []
    if args.brief:
        brief_path = Path(args.brief)
        brief = json.loads(brief_path.read_text(encoding="utf-8"))
        findings.extend(scan_brief(brief, str(brief_path)))

    for raw_path in args.text:
        path = Path(raw_path)
        if not path.exists():
            findings.append({"label": str(path), "risk": "missing file", "match": "", "snippet": "File does not exist"})
            continue
        findings.extend(scan_text(path.read_text(encoding="utf-8", errors="ignore"), str(path)))

    print(dumps_result(findings))
    return 0 if not findings else 1


if __name__ == "__main__":
    raise SystemExit(main())
