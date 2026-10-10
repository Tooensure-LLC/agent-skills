#!/usr/bin/env python3
"""Validate the deterministic PMCR-O packet used by slow local models."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


REQUIRED = (
    "apiVersion",
    "trailId",
    "cycleId",
    "phase",
    "iAm",
    "executionTarget",
    "installation",
    "userActions",
    "agentActions",
    "evidence",
    "status",
    "nextSeed",
)
TARGETS = {"export-guide", "browser-session", "desktop-session"}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--packet", type=Path, required=True)
    args = parser.parse_args()
    packet = json.loads(args.packet.read_text(encoding="utf-8"))
    missing = [field for field in REQUIRED if field not in packet]
    if missing:
        raise SystemExit(f"FAIL: missing fields: {', '.join(missing)}")
    if packet["apiVersion"] != "pmcro.execution-packet/v1":
        raise SystemExit("FAIL: unsupported packet version")
    if packet["executionTarget"] not in TARGETS:
        raise SystemExit("FAIL: unknown execution target")
    if not isinstance(packet["userActions"], list) or not packet["userActions"]:
        raise SystemExit("FAIL: userActions must contain at least one step")
    if not isinstance(packet["agentActions"], list) or not packet["agentActions"]:
        raise SystemExit("FAIL: agentActions must contain at least one step")
    if packet["nextSeed"].get("unexecuted") is not True:
        raise SystemExit("FAIL: next seed must be explicitly unexecuted")
    if packet["executionTarget"] == "export-guide" and packet["installation"].get("agentMayInstall") is not False:
        raise SystemExit("FAIL: export-guide cannot authorize agent installation")
    print(f"PASS: execution packet; target={packet['executionTarget']}; user_steps={len(packet['userActions'])}; agent_steps={len(packet['agentActions'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
