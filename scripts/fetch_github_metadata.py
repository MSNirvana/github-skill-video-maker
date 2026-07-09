#!/usr/bin/env python3
"""Fetch structured GitHub repository metadata for video production."""

from __future__ import annotations

import argparse
import html
import json
import os
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path


def parse_repo(value: str) -> tuple[str, str]:
    value = value.strip().removesuffix("/")
    match = re.search(r"github\.com[:/](?P<owner>[^/\s]+)/(?P<repo>[^/\s#?]+)", value)
    if match:
        return match.group("owner"), match.group("repo").removesuffix(".git")
    if re.match(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$", value):
        owner, repo = value.split("/", 1)
        return owner, repo.removesuffix(".git")
    raise ValueError(f"Expected GitHub URL or owner/repo, got: {value}")


def request_json(url: str, headers: dict[str, str]) -> dict | list:
    request = urllib.request.Request(
        url,
        headers=headers,
    )
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")[:500]
        raise RuntimeError(f"HTTP {exc.code} for {url}: {detail}") from exc


def request_text(url: str) -> str:
    request = urllib.request.Request(
        url,
        headers={
            "Accept": "text/html,application/xhtml+xml",
            "User-Agent": "github-skill-video-maker",
        },
    )
    with urllib.request.urlopen(request, timeout=20) as response:
        return response.read().decode("utf-8", errors="replace")


def github_json(path: str) -> dict | list:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "github-skill-video-maker",
    }
    if os.environ.get("GITHUB_TOKEN"):
        headers["Authorization"] = f"Bearer {os.environ['GITHUB_TOKEN']}"
    return request_json(f"https://api.github.com{path}", headers)


def compact_star_count(stars: int) -> str:
    if stars >= 1_000_000:
        return f"{stars / 1_000_000:.1f}m".replace(".0m", "m")
    if stars >= 100_000:
        return f"{round(stars / 1000):.0f}k+"
    if stars >= 10_000:
        return f"{stars / 1000:.1f}k".replace(".0k", "k")
    if stars >= 1000:
        return f"{stars / 1000:.1f}k".replace(".0k", "k")
    return str(stars)


def parse_meta_content(page: str, pattern: str) -> str:
    match = re.search(pattern, page, re.S)
    if not match:
        return ""
    return html.unescape(match.group(1)).strip()


def fetch_html_fallback(owner: str, repo: str, error: str) -> dict:
    url = f"https://github.com/{owner}/{repo}"
    page = request_text(url)
    page_title = parse_meta_content(page, r'<meta property="og:title" content="([^"]*)"')
    description = parse_meta_content(page, r'<meta property="og:description" content="([^"]*)"')
    description = re.sub(rf"\s*-\s*{re.escape(owner)}/{re.escape(repo)}\s*$", "", description).strip()

    stars = 0
    stars_label = ""
    star_patterns = [
        r'title="([0-9,]+)"[^>]*class="Counter js-social-count"[^>]*>([^<]+)<',
        r'class="Counter js-social-count"[^>]*title="([0-9,]+)"[^>]*>([^<]+)<',
    ]
    for pattern in star_patterns:
        match = re.search(pattern, page, re.S)
        if match:
            stars = int(match.group(1).replace(",", ""))
            stars_label = html.unescape(match.group(2)).strip()
            break
    if stars and not stars_label:
        stars_label = compact_star_count(stars)

    branch_match = re.search(r'/archive/refs/heads/([^"/]+)\.zip', page)
    default_branch = html.unescape(branch_match.group(1)) if branch_match else "main"

    topics = [
        html.unescape(topic).strip()
        for topic in re.findall(r'topic-tag[^>]*>\s*([^<]+)\s*</a>', page, re.S)
        if topic.strip()
    ]

    return {
        "owner": owner,
        "repo": repo,
        "full_name": f"{owner}/{repo}",
        "page_title": page_title,
        "html_url": url,
        "description": description,
        "stars": stars,
        "stars_label": compact_star_count(stars) if stars else stars_label,
        "forks": 0,
        "watchers": 0,
        "license": "",
        "topics": topics,
        "default_branch": default_branch,
        "language": "",
        "latest_release": "",
        "recent_tags": [],
        "open_issues": 0,
        "captured_at": datetime.now(timezone.utc).isoformat(),
        "source": "GitHub HTML fallback",
        "source_warning": error,
    }


def fetch_metadata(owner: str, repo: str) -> dict:
    try:
        data = github_json(f"/repos/{owner}/{repo}")
    except RuntimeError as exc:
        return fetch_html_fallback(owner, repo, str(exc))

    latest_release = None
    try:
        latest_release = github_json(f"/repos/{owner}/{repo}/releases/latest")
    except RuntimeError:
        latest_release = None

    tags = []
    try:
        tag_data = github_json(f"/repos/{owner}/{repo}/tags?per_page=5")
        tags = [item.get("name") for item in tag_data if item.get("name")]
    except RuntimeError:
        tags = []

    stars = int(data.get("stargazers_count") or 0)
    return {
        "owner": owner,
        "repo": repo,
        "full_name": data.get("full_name", f"{owner}/{repo}"),
        "html_url": data.get("html_url", f"https://github.com/{owner}/{repo}"),
        "description": data.get("description") or "",
        "stars": stars,
        "stars_label": compact_star_count(stars),
        "forks": data.get("forks_count") or 0,
        "watchers": data.get("subscribers_count") or data.get("watchers_count") or 0,
        "license": (data.get("license") or {}).get("spdx_id") or "",
        "topics": data.get("topics") or [],
        "default_branch": data.get("default_branch") or "main",
        "language": data.get("language") or "",
        "latest_release": (latest_release or {}).get("tag_name") or "",
        "recent_tags": tags,
        "open_issues": data.get("open_issues_count") or 0,
        "captured_at": datetime.now(timezone.utc).isoformat(),
        "source": "GitHub API",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Fetch GitHub metadata for a repo video.")
    parser.add_argument("repo", help="GitHub URL or owner/repo")
    parser.add_argument("--output", "-o", required=True, help="Output JSON path")
    args = parser.parse_args()

    owner, repo = parse_repo(args.repo)
    metadata = fetch_metadata(owner, repo)

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({
        "output": str(output),
        "full_name": metadata["full_name"],
        "stars": metadata["stars"],
        "source": metadata["source"],
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
