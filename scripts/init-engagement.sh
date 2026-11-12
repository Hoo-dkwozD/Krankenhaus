#!/usr/bin/env bash
set -euo pipefail

ROOT="$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)"

mkdir -p "$ROOT/private" "$ROOT/evidence" "$ROOT/findings" "$ROOT/plans"
chmod 700 "$ROOT/private"

for source in \
  "$ROOT/engagement/Engagement-Info.md" \
  "$ROOT/engagement/Roles-and-Credentials.md" \
  "$ROOT/engagement/Endpoint-Notes.md" \
  "$ROOT/engagement/Input-Point-Notes.md"; do
  if [[ ! -f "$source" ]]; then
    echo "Missing human-readable source: $source" >&2
    exit 1
  fi
done

"$ROOT/scripts/build-machine-state.py"

cat <<'EOF'
Initialization complete.

Before target traffic:
  1. Fill the human-readable files under engagement/.
  2. Fill catalogue/Finding-Catalogue.md with applicable finding objectives.
  3. Run scripts/build-machine-state.py after every source change.
  4. Add credentials only to ignored private/ storage or a password manager.
  5. Review generated config/*.yaml/csv, plans/*.csv, and plans/Finding-Plan.md.
  6. Confirm Burp MCP and the authorized testing window.
EOF
