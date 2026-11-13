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
"$ROOT/scripts/build-llm-state.py"

cat <<'EOF'
Initialization complete.

Before target traffic:
  1. Fill the human-readable files under engagement/ and, if using it, llm/engagement/.
  2. Fill catalogue/Finding-Catalogue.md and review the applicable resource-bank family sources.
  3. If LLM mode is active, review llm/playbooks/Playbook-Index.md and select the approved integration.
  4. Run scripts/build-machine-state.py and/or scripts/build-llm-state.py after source changes.
  5. Add credentials only to ignored private/ storage or a password manager.
  6. Review generated web-app state, context-bank references, and llm/generated/LLM-Finding-Plan.md.
  7. Confirm Burp MCP, LLM target adapter allowlists, selected playbook/policy gates, kill switch, and authorized testing windows.
EOF
