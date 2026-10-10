#!/usr/bin/env python3
"""Create the smallest PMCR-O activation packet for capcut-agent."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


TARGETS = {"export-guide", "browser-session", "desktop-session"}


def packet(intent: str, owner: str, target: str) -> dict:
    requested_target = target or "export-guide"
    target = requested_target
    fallback_reason = None
    if target not in TARGETS:
        fallback_reason = f"Unknown target '{target}'; resolved to export-guide."
        target = "export-guide"
    needs_capability = target != "export-guide"
    value = {
        "apiVersion": "pmcro.activation/v1",
        "command": "init",
        "activationId": "capcut-agent-init",
        "trailId": "tooensure-capcut-agent-trail",
        "cycleId": "capcut-init-001",
        "phase": "orchestrate",
        "iAm": {"agent": "tooensure.capcut.agent", "role": "orchestrator", "authority": "domain-grant-only"},
        "owner": owner,
        "intent": intent,
        "selection": {
            "requestedTarget": requested_target,
            "resolvedTarget": target,
            "fallback": fallback_reason is not None,
        },
        "target": target,
        "mode": "export-guide" if target == "export-guide" else "capability-check",
        "autonomyLevel": 0 if target == "export-guide" else 1 if target == "browser-session" else 2,
        "installation": {"owner": "user-directed", "required": target == "desktop-session", "agentMayInstall": False},
        "capabilityCheckRequired": needs_capability,
        "userActions": [
            "Confirm the target and the intended export settings.",
            "If browser-session or desktop-session is selected, confirm the platform surface is available."
        ],
        "agentActions": [
            "Read the PMCR-O manifest and target contract.",
            "Return the next phase as a numbered, observable task.",
            "Do not install, authenticate, open CapCut, or claim an export."
        ],
        "status": "ready-for-target-confirmation",
        "evidence": ["activation-packet", "target-confirmation"],
        "nextSeed": {
            "level": "meta1",
            "unexecuted": True,
            "promptIntent": "Confirm the target, then route only to the capability declared by the active platform."
        }
    }
    if fallback_reason:
        value["selection"]["reason"] = fallback_reason
    return value


def render_text(value: dict) -> str:
    return "\n".join([
        "PMCR-O FRAME: orchestrate",
        f"I AM: {value['iAm']['agent']} ({value['iAm']['role']})",
        f"TARGET: {value['target']}",
        f"INTENT: {value['intent']}",
        "USER ACTIONS:",
        *[f"{i}. {item}" for i, item in enumerate(value["userActions"], 1)],
        "AGENT ACTIONS:",
        *[f"{i}. {item}" for i, item in enumerate(value["agentActions"], 1)],
        f"STATUS: {value['status']}",
        "NEXT SEED: unexecuted; confirm target and platform capability."
    ])


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--intent", default="Prepare a CapCut project for export using the safest available target.")
    parser.add_argument("--owner", default="user")
    parser.add_argument("--target", default="export-guide")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()
    value = packet(args.intent, args.owner, args.target)
    output = json.dumps(value, indent=2) if args.json else render_text(value)
    if args.out:
        args.out.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
