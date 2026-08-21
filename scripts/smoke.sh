#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
PYTHONPATH=src python3 -m unittest discover -s tests -v
PYTHONPATH=src python3 -m owp.cli demo --json
