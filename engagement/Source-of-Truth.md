# Source-of-Truth Workflow

Users edit only human-readable files:

- `Engagement-Info.md` — scope, dates, tooling, approvals, and engagement notes.
- `Roles-and-Credentials.md` — role order, usernames, tenants, and secret references; never passwords.
- `Task-Info.md` — assistant operating instructions and safety boundaries.
- `Checklist.md` — human execution checklist.
- `Endpoint-Notes.md` — reconnaissance endpoint inventory.
- `Input-Point-Notes.md` — input/entry-point mapping.
- `catalogue/Finding-Catalogue.md` — reusable finding objectives and engagement-specific additions.

Generated files are machine-readable or derived outputs and must not be edited manually:

- `config/engagement.yaml`
- `config/roles.csv`
- `plans/Endpoint-Inventory.csv`
- `plans/Input-Point-Inventory.csv`
- `plans/Finding-Plan.md`

After editing human-readable sources, run:

```bash
./scripts/build-machine-state.py
```

That command regenerates the machine-readable configuration, inventories, and finding plan. Regeneration is deterministic: a later run replaces derived content with the current Markdown source values.
