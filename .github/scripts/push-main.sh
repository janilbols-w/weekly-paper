#!/usr/bin/env bash
set -euo pipefail

for attempt in 1 2 3; do
  git pull --rebase origin main
  if git push origin HEAD:main; then
    git fetch origin main
    git merge-base --is-ancestor HEAD origin/main
    exit 0
  fi
  if [[ "$attempt" == "3" ]]; then
    echo "Failed to push main after $attempt attempts" >&2
    exit 1
  fi
  sleep "$attempt"
done
