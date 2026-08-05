#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
REFERENCE_DATE="$(TZ=Asia/Shanghai date +%F)"

cd "$ROOT"
"$ROOT/.venv/bin/python" -m weekly_paper.cli \
  --reference-date "$REFERENCE_DATE" \
  --weeks-back "${WEEKS_BACK:-1}" \
  "$@"

