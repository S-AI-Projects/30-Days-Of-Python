"""Minimal zero-dependency PEP 517 build backend for the Day 29 mini-package lab."""

from __future__ import annotations

import base64
import hashlib
import os
import zipfile
from pathlib import Path
from typing import Dict, List, Optional

DIST_NAME = "r27_t029_wordcount"
VERSION = "0.1.0"
DIST_INFO = f"{DIST_NAME}-{VERSION}.dist-info"


def _hash_bytes(data: bytes) -> str:
    digest = hashlib.sha256(data).digest()
    b64 = base64.urlsafe_b64encode(digest).rstrip(b"=").decode("ascii")
    return f"sha256={b64},{len(data)}"


def get_requires_for_build_wheel(config_settings: Optional[Dict[str, object]] = None) -> List[str]:
    return []


def get_requires_for_build_editable(config_settings: Optional[Dict[str, object]] = None) -> List[str]:
    return []


def build_wheel(
    wheel_directory: str,
    config_settings: Optional[Dict[str, object]] = None,
    metadata_directory: Optional[str] = None,
) -> str:
    root = Path(__file__).resolve().parent
    pkg_dir = root / "wordcount_pkg"
    wheel_name = f"{DIST_NAME}-{VERSION}-py3-none-any.whl"
    wheel_path = Path(wheel_directory) / wheel_name

    files: Dict[str, bytes] = {}
    for py_file in sorted(pkg_dir.glob("*.py")):
        rel_arc = f"wordcount_pkg/{py_file.name}"
        files[rel_arc] = py_file.read_bytes()

    files[f"{DIST_INFO}/METADATA"] = (
        "Metadata-Version: 2.1\n"
        "Name: r27-t029-wordcount\n"
        f"Version: {VERSION}\n"
        "Summary: Day 29 installable mini-package exposing word_count and CLI entry point\n"
    ).encode("utf-8")

    files[f"{DIST_INFO}/WHEEL"] = (
        "Wheel-Version: 1.0\n"
        "Generator: r27-t029-pep517\n"
        "Root-Is-Purelib: true\n"
        "Tag: py3-none-any\n"
    ).encode("utf-8")

    files[f"{DIST_INFO}/entry_points.txt"] = (
        "[console_scripts]\n"
        "r27-wordcount = wordcount_pkg.cli:main\n"
    ).encode("utf-8")

    record_lines: List[str] = []
    with zipfile.ZipFile(wheel_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for arcname, content in files.items():
            zf.writestr(arcname, content)
            record_lines.append(f"{arcname},{_hash_bytes(content)}")
        record_arc = f"{DIST_INFO}/RECORD"
        record_lines.append(f"{record_arc},,")
        zf.writestr(record_arc, "\n".join(record_lines) + "\n")

    return wheel_name


build_editable = build_wheel
