#!/usr/bin/env python3
"""Capture GitHub screenshots and stable crops for repo explainer videos."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path
from urllib.parse import quote

try:
    from PIL import Image
except Exception:  # pragma: no cover - optional crop support
    Image = None


DEFAULT_CHROME_PATHS = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    "google-chrome",
    "chromium",
    "chromium-browser",
]


def find_chrome(explicit: str = "") -> str:
    if explicit:
        return explicit
    for candidate in DEFAULT_CHROME_PATHS:
        if "/" in candidate and Path(candidate).exists():
            return candidate
        found = shutil.which(candidate)
        if found:
            return found
    raise RuntimeError("Chrome/Chromium not found. Pass --chrome /path/to/chrome.")


def run_chrome(chrome: str, url: str, output: Path, width: int, height: int) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        chrome,
        "--headless=new",
        "--disable-gpu",
        "--no-first-run",
        "--no-default-browser-check",
        "--hide-scrollbars",
        f"--window-size={width},{height}",
        f"--screenshot={output}",
        url,
    ]
    subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def crop(image_path: Path, output_path: Path, box: tuple[int, int, int, int]) -> bool:
    if Image is None:
        return False
    with Image.open(image_path) as image:
        image.crop(box).save(output_path)
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description="Capture GitHub screenshots for a repo video.")
    parser.add_argument("repo", help="GitHub URL or owner/repo")
    parser.add_argument("--output-dir", "-o", required=True)
    parser.add_argument("--paths", nargs="*", default=[], help="Repo paths to capture, e.g. skills README.md skills/foo/SKILL.md")
    parser.add_argument("--branch", default="main", help="Branch/ref used for repo paths")
    parser.add_argument("--chrome", default="")
    parser.add_argument("--width", type=int, default=1440)
    parser.add_argument("--height", type=int, default=1100)
    args = parser.parse_args()

    repo = args.repo.strip().removesuffix("/")
    if "github.com" not in repo:
        repo = f"https://github.com/{repo}"
    chrome = find_chrome(args.chrome)
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    captures: dict[str, str] = {}
    repo_png = out_dir / "github-repo.png"
    run_chrome(chrome, repo, repo_png, args.width, args.height)
    captures["repo"] = str(repo_png)

    # These crops match the default 1440x1100 GitHub layout. They are used as
    # source material, not as truth; verify visually before final render.
    if crop(repo_png, out_dir / "github-repo-header.png", (0, 95, 1440, 245)):
        captures["repo_header"] = str(out_dir / "github-repo-header.png")
    if crop(repo_png, out_dir / "github-repo-identity-stars.png", (0, 95, 1440, 185)):
        captures["repo_identity_stars"] = str(out_dir / "github-repo-identity-stars.png")
    if crop(repo_png, out_dir / "github-star-actions.png", (930, 110, 1435, 205)):
        captures["star_actions"] = str(out_dir / "github-star-actions.png")
    if crop(repo_png, out_dir / "github-about-stars.png", (1010, 590, 1428, 875)):
        captures["about_stars"] = str(out_dir / "github-about-stars.png")

    for raw_path in args.paths:
        clean = raw_path.strip("/")
        if not clean:
            continue
        kind = "tree" if "." not in Path(clean).name else "blob"
        branch_url = f"{repo}/{kind}/{quote(args.branch, safe='')}/{quote(clean, safe='/')}"
        safe = clean.replace("/", "__").replace(".", "_")
        output = out_dir / f"github-{safe}.png"
        run_chrome(chrome, branch_url, output, args.width, args.height)
        captures[clean] = str(output)

    manifest = {
        "repo_url": repo,
        "chrome": chrome,
        "viewport": {"width": args.width, "height": args.height},
        "captures": captures,
        "notes": "Keep original captures for audit. Prefer repo_identity_stars for public distribution, then verify all final crops remove URLs, QR/contact details, clone/download/install controls, and unrelated outbound calls to action.",
    }
    manifest_path = out_dir / "screenshots-manifest.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"manifest": str(manifest_path), "count": len(captures)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
