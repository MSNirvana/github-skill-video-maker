#!/usr/bin/env python3
"""Shared external-channel risk checks for public-platform video text."""

from __future__ import annotations

import json
import re
from typing import Any


RISK_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    (
        "raw URL or domain",
        re.compile(
            r"https?://|www\.|(?:[a-z0-9-]+\.)+(?:com|cn|net|org|io|ai|app)(?:[/\s]|$)",
            re.IGNORECASE,
        ),
    ),
    ("external address language", re.compile(r"项目地址|仓库地址|访问地址|官网地址|外链")),
    ("anti-evasion or external-routing language", re.compile(r"站外|引流|绕过审核|规避风控")),
    ("QR or contact routing", re.compile(r"二维码|扫码|加我|加微信|加V|私信(?:我|获取|领取|发送|发你)?", re.IGNORECASE)),
    (
        "comment/profile delivery",
        re.compile(r"(?:评论区|主页|置顶).{0,12}(?:获取|领取|链接|地址|下载|安装|发你|去看)"),
    ),
    (
        "outbound action instruction",
        re.compile(r"(?:点击|复制|打开|访问|前往|跳转|进入|去).{0,10}(?:链接|网址|网站|官网|GitHub|应用|小程序|软件)", re.IGNORECASE),
    ),
    (
        "third-party download or installation instruction",
        re.compile(r"(?:下载|安装|克隆|注册|使用).{0,10}(?:第三方|软件|应用|客户端|插件|小程序|网站|工具)"),
    ),
    ("public download or installation language", re.compile(r"下载|安装|克隆仓库|注册账号")),
]


def flatten_text(value: Any) -> list[str]:
    if isinstance(value, str):
        return [value]
    if isinstance(value, dict):
        result: list[str] = []
        for item in value.values():
            result.extend(flatten_text(item))
        return result
    if isinstance(value, list):
        result = []
        for item in value:
            result.extend(flatten_text(item))
        return result
    return []


def public_brief_text(brief: dict[str, Any]) -> str:
    subtitles = brief.get("subtitle_strategy", {}) or {}
    payload = {
        "hook": brief.get("hook", {}),
        "why_watch": brief.get("why_watch", ""),
        "cover_hook": brief.get("cover_hook", ""),
        "cta": brief.get("cta", ""),
        "creator_signature": brief.get("creator_signature", {}),
        "viral_packaging": brief.get("viral_packaging", {}),
        "insight_subtitles": subtitles.get("insight_subtitles", []),
        "line_subtitles": subtitles.get("line_subtitles", []),
        "platform_safety_note": brief.get("platform_safety_note", {}),
    }
    return "\n".join(flatten_text(payload))


def scan_text(text: str, label: str = "text") -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    for risk, pattern in RISK_PATTERNS:
        match = pattern.search(text)
        if not match:
            continue
        start = max(0, match.start() - 30)
        end = min(len(text), match.end() + 30)
        snippet = re.sub(r"\s+", " ", text[start:end]).strip()
        findings.append({"label": label, "risk": risk, "match": match.group(0), "snippet": snippet})
    return findings


def scan_brief(brief: dict[str, Any], label: str = "brief public text") -> list[dict[str, str]]:
    return scan_text(public_brief_text(brief), label)


def result_payload(findings: list[dict[str, str]]) -> dict[str, Any]:
    return {"ok": not findings, "finding_count": len(findings), "findings": findings}


def dumps_result(findings: list[dict[str, str]]) -> str:
    return json.dumps(result_payload(findings), ensure_ascii=False, indent=2)
