# Source-of-Truth Workflow

Users edit only human-readable files.

## Web-application mode

- `Engagement-Info.md` — scope, dates, tooling, approvals, and engagement notes.
- `Roles-and-Credentials.md` — role order, usernames, tenants, and secret references; never passwords.
- `Task-Info.md` — assistant operating instructions and safety boundaries.
- `Checklist.md` — human execution checklist.
- `Endpoint-Notes.md` — reconnaissance endpoint inventory.
- `Input-Point-Notes.md` — input/entry-point mapping.
- `catalogue/Finding-Catalogue.md` — reusable finding objectives and engagement-specific additions.

## Shared resource bank

- `resource-bank/Resource-Locator.md` — local/online resource locators, provenance, version, license, and approval notes.
- `resource-bank/<family>/` — vulnerability-family resource structures.


## Context-bank and playbook gate

The resource bank is the shared context bank for web-application findings. After reconnaissance and surface mapping, select the applicable family resources from `resource-bank/Resource-Locator.md` and record their IDs, versions, provenance, applicability, and exclusions in the engagement notes. Do not treat a resource entry as an instruction to send every payload.

For LLM mode, select the applicable reviewed playbook from `llm/playbooks/Playbook-Index.md` and record the selected integration in the campaign plan. A playbook supplies approved procedures and evaluation guidance; it does not authorize or activate a campaign by itself.

## LLM testing mode

- `llm/engagement/LLM-Engagement-Info.md` — business/user context, authorization, model/evidence/budget details.
- `llm/engagement/LLM-Target-Context.md` — exact prompt-insertion endpoint and adapter contract.
- `llm/engagement/LLM-Policy-Matrix.md` — context-specific policy and evaluation oracle.
- `llm/engagement/LLM-Testing-Plan.md` — dynamic objective list and campaign sequence.
- `llm/playbooks/` — reviewed LLM playbooks and integrations.

Generated files are machine-readable or derived outputs and must not be edited manually:

- `config/engagement.yaml`
- `config/roles.csv`
- `plans/Endpoint-Inventory.csv`
- `plans/Input-Point-Inventory.csv`
- `plans/Finding-Plan.md`
- `llm/generated/llm-engagement.yaml`
- `llm/generated/llm-targets.csv`
- `llm/generated/llm-policy-matrix.csv`
- `llm/generated/llm-campaign-matrix.csv`
- `llm/generated/LLM-Finding-Plan.md`

After editing web-app sources, run:

```bash
./scripts/build-machine-state.py
```

After editing LLM sources, run:

```bash
./scripts/build-llm-state.py
```

Each command regenerates its mode's machine-readable state deterministically.

