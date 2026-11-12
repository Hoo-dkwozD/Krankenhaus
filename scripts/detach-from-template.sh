#!/usr/bin/env bash
set -euo pipefail

if [[ "${1:-}" != "--confirm" ]]; then
  echo "Refusing to remove Git metadata. Re-run with --confirm from the project root." >&2
  exit 2
fi

ROOT="$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)"
[[ -d "$ROOT/.git" ]] || { echo "No root .git directory found; nothing changed."; exit 0; }

rm -rf "$ROOT/.git"
find "$ROOT" -mindepth 2 -type d -name .git -prune -exec rm -rf {} +
echo "Removed Git metadata from $ROOT. The project is now detached from the template repository."
