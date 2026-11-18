#!/usr/bin/env bash
set -euo pipefail

ROOT="$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)"

mkdir -p "$ROOT/private" "$ROOT/evidence" "$ROOT/findings" "$ROOT/plans"
chmod 700 "$ROOT/private"

for source in \
  "$ROOT/engagement/Engagement-Info.md" \
  "$ROOT/engagement/Roles-and-Credentials.md" \
  "$ROOT/engagement/Task-Info.md" \
  "$ROOT/engagement/Checklist.md" \
  "$ROOT/catalogue/Finding-Catalogue.md" \
  "$ROOT/resource-bank/Resource-Locator.md"; do
  if [[ ! -f "$source" ]]; then
    echo "Missing human-readable source: $source" >&2
    exit 1
  fi
done

cat <<'EOF'
Workspace initialized.

Before target traffic:
  1. Fill the target URL, Burp MCP endpoint (default http://127.0.0.1:9876), credential references, supplied roles, and any optional notes.
  2. Read all engagement sources, the finding catalogue, and the resource-bank sources.
  3. Retrieve and review each applicable enabled online resource; record the extracted references in plans/Resource-Review.md.
  4. Build plans/Operational-State.md, plans/Finding-Plan.md, plans/Endpoint-Inventory.md,
     plans/Input-Point-Inventory.md, and plans/Protected-Operations.md directly.
  5. Use Burp MCP as the primary interface; review its sitemap/history and perform request-based testing there.
  6. Use the direct browser only for a recorded MCP/tooling, rendering, browser-state, visual, or interaction-specific gap.
  7. Test every mapped boundary and every distinct valid instance; do not stop after the first finding.
  8. Do not run denial-of-service or unbounded load testing. Keep rate-limit testing bounded.
EOF
