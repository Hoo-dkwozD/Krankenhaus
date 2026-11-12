#!/usr/bin/env bash
set -euo pipefail

ROOT="$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)"

mkdir -p "$ROOT/private" "$ROOT/evidence" "$ROOT/findings" "$ROOT/plans"
chmod 700 "$ROOT/private"

if [[ ! -f "$ROOT/config/engagement.yaml" || ! -f "$ROOT/config/roles.csv" ]]; then
  echo "Missing config/engagement.yaml or config/roles.csv" >&2
  exit 1
fi

"$ROOT/scripts/build-finding-plan.py"

cat <<'EOF'
Initialization complete.

Before target traffic:
  1. Fill engagement/Engagement-Info.md.
  2. Fill engagement/Task-Info.md with engagement-specific boundaries.
  3. Fill config/engagement.yaml and config/roles.csv without storing secrets.
  4. Add credentials only to ignored private/ storage or a password manager.
  5. Review plans/Finding-Plan.md, plans/Endpoint-Inventory.csv, and plans/Input-Point-Inventory.csv.
  6. Confirm Burp MCP and the authorized testing window.
EOF
