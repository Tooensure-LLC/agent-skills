#!/usr/bin/env python3
"""Skill-local wrapper for the product-level CapCut activation entrypoint."""

from pathlib import Path
import runpy


PRODUCT_ROOT = Path(__file__).resolve().parents[3]
runpy.run_path(str(PRODUCT_ROOT / "scripts" / "init.py"), run_name="__main__")
