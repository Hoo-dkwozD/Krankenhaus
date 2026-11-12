#!/usr/bin/env bash
set -euo pipefail

usage() {
  echo "Usage: $0 --destination /path/to/new-project"
  echo "Copies this template without Git metadata; it does not contact a target."
}

DEST_INPUT=""
while [[ $# -gt 0 ]]; do
  case "$1" in
    --destination)
      [[ $# -ge 2 ]] || { usage >&2; exit 2; }
      DEST_INPUT="$2"
      shift 2
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown option: $1" >&2
      usage >&2
      exit 2
      ;;
  esac
done

[[ -n "$DEST_INPUT" ]] || { usage >&2; exit 2; }
SOURCE="$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)"
DEST_INPUT="$(CDPATH= cd -- "$(dirname -- "$DEST_INPUT")" && printf '%s/%s' "$PWD" "$(basename -- "$DEST_INPUT")")"

if [[ -e "$DEST_INPUT" ]]; then
  if [[ -n "$(find "$DEST_INPUT" -mindepth 1 -maxdepth 1 -print -quit 2>/dev/null)" ]]; then
    echo "Refusing non-empty destination: $DEST_INPUT" >&2
    exit 1
  fi
else
  mkdir -p "$DEST_INPUT"
fi

# BSD tar is available on macOS and preserves the tree while excluding Git metadata.
tar -C "$SOURCE" --exclude='./.git' --exclude='./.DS_Store' -cf - . | tar -C "$DEST_INPUT" -xf -
find "$DEST_INPUT" -type d -name .git -prune -exec rm -rf {} +
"$DEST_INPUT/scripts/init-engagement.sh"

echo "Created detached engagement project: $DEST_INPUT"
