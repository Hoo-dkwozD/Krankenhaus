# Source-of-Truth Workflow

Humans provide the small set of engagement inputs. The LLM reads those inputs, the current target surface, Burp MCP data, the finding catalogue, and the resource bank, then maintains the operational working state directly.

## Human-readable engagement inputs

- `engagement/Engagement-Info.md` — target URL, Burp MCP endpoint, optional scope, browser fallback notes, test-data/cleanup notes, and free-form context.
- `engagement/Roles-and-Credentials.md` — supplied roles, usernames, credential references, and optional role context.
- `engagement/Task-Info.md` — extensive testing workflow, exhaustive coverage rules, resource reading, UI/API comparison, and minimal operating constraints.
- `engagement/Checklist.md` — practical coverage gate.
- `engagement/Endpoint-Notes.md` — optional reconnaissance notes.
- `engagement/Input-Point-Notes.md` — optional starting input notes.
- `catalogue/Finding-Catalogue.md` — reusable finding objectives.

## Shared resource bank

- `resource-bank/README.md` — resource-bank purpose and engagement use.
- `resource-bank/Resource-Locator.md` — local/online resources, provenance, dates, licenses, applicability, and review status.
- `resource-bank/<family>/` — vulnerability-family research structures.

## LLM-maintained working state

The LLM MUST create or update these files before and during testing:

- `plans/Operational-State.md` — current target, roles, sitemap, technologies, workflows, UI/API comparison, and scope assumptions.
- `plans/Finding-Plan.md` — complete surface-driven finding objectives and coverage status.
- `plans/Endpoint-Inventory.md` — all endpoint, method, protocol, UI, API, and WebSocket surfaces.
- `plans/Input-Point-Inventory.md` — all input points, sinks, contexts, roles, and test batches.
- `plans/Protected-Operations.md` — operations each role should and should not reach.
- `plans/Resource-Review.md` — online/local references read, relevant sections extracted, technique variants, dates, limitations, and applicability.

These files are working state, not generated output. No human-readable-to-machine-readable conversion script is required.

## LLM mode

LLM testing remains a separate workstream. Its human-readable context and playbook files are under `llm/engagement/` and `llm/playbooks/`. The LLM reads them and maintains campaign state directly; it does not require a build script or generated state directory.

## Security of local material

Keep passwords, tokens, API keys, raw PII, raw Burp projects, uncontrolled exports, and sensitive transcripts in ignored `private/` or approved secure storage. This is a storage rule, not a per-test approval workflow.
