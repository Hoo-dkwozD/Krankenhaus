```text
                       _              _                     
  /\ /\_ __ __ _ _ __ | | _____ _ __ | |__   __ _ _   _ ___ 
 / //_/ '__/ _` | '_ \| |/ / _ \ '_ \| '_ \ / _` | | | / __|
/ __ \| | | (_| | | | |   <  __/ | | | | | | (_| | |_| \__ \
\/  \/|_|  \__,_|_| |_|_|\_\___|_| |_|_| |_|\__,_|\__,_|___/
                                                            
```

# Krankenhaus

Reusable workspace for extensive authorized web-application security assessments.

## Design goals

- Keep human input small: target URL, credential references, roles, and optional notes.
- Let the LLM read, reconcile, and maintain operational state directly; no source-to-machine conversion scripts.
- Build the finding plan from the current sitemap, UI/API map, technologies, roles, and resource review.
- Test every valid instance across every reachable role and relevant input or protocol boundary.
- Compare UI behavior with direct API and WebSocket behavior instead of treating the UI as the complete security boundary.
- Use current online resources for current encodings, parser differences, payload variants, and defensive expectations.

## Repository layout

```text
engagement/                  Minimal human-readable web-app inputs and optional notes
catalogue/                   Human-readable finding objectives
plans/                       LLM-maintained operational state, inventories, coverage, and resource review
resource-bank/               Vulnerability-family resources and online locators
llm/                         Separate LLM-mode context and playbooks
templates/                   Evidence and finding-record templates
scripts/                     Project-copy and workspace setup helpers only
evidence/                    Sanitized web-app evidence
findings/                    Web-app finding records and remediation notes
private/                     Local-only credential references and sensitive material
docs/                        Optional showcase documentation
```

## New engagement workflow

1. Clone the repository as a reusable template.

   ```bash
   git clone <template-repository-url> <template-clone>
   cd <template-clone>
   ```

2. Create a detached project copy. It contains no Git metadata:

   ```bash
   ./scripts/new-engagement.sh \
     --destination "$HOME/Documents/Security Engagements/<Project>"
   ```

3. Fill only the small human-readable input set:

   - `engagement/Engagement-Info.md` — primary URL, Burp MCP endpoint, and optional notes.
   - `engagement/Roles-and-Credentials.md` — supplied roles and secret references.
   - Optional endpoint or input starting notes.
   - `catalogue/Finding-Catalogue.md` — reusable objectives and additions.

4. Before testing, the LLM reads every applicable engagement file, the finding catalogue, the resource-bank overview and locator, and the relevant local or online resources. It retrieves enabled online references, extracts the current relevant techniques and defensive expectations, and records the review in `plans/Resource-Review.md`.

5. The LLM creates or updates `plans/Operational-State.md`, `plans/Finding-Plan.md`, `plans/Endpoint-Inventory.md`, `plans/Input-Point-Inventory.md`, and `plans/Protected-Operations.md` from the current target, configured Burp MCP sitemap/history, UI behavior, roles, technologies, and resource review.

6. Burp MCP is the primary testing interface for traffic, reconnaissance, sitemap/history review, request replay and mutation, API/WebSocket testing, comparison, and evidence. Direct browser use is only a fallback for behavior Burp MCP cannot expose or exercise; the reason and attempted MCP coverage must be recorded.

7. The LLM reconciles every UI workflow with its API or WebSocket behavior, maps every input and protocol surface, and builds the complete finding plan. It then tests all applicable findings, all mapped inputs, all supplied roles, and all distinct valid instances. It does not stop after the first finding.

8. Keep the working plans current throughout testing. The plans are not generated artifacts and no conversion command is required.


## Testing principles
- Use the configured Burp MCP connection for testing by default; use the direct browser only for a recorded MCP/tooling, rendering, browser-state, visual, or interaction-specific gap.

- Use the role order supplied for the engagement; do not assume Super Admin, Admin, Supervisor, Agent, tenants, or any other fixed model.
- Treat meaningful UI/API differences in authorization, validation, data, state changes, errors, and side effects as candidate weaknesses requiring confirmation.
- Use current resource references for XSS, SQLi, headers, parser behavior, encoding, framework-specific sinks, and other applicable families.
- Test headers across HTML, API, asset, redirect, authentication, error, and download responses, including missing, weak, contradictory, inconsistent, obsolete, and deprecated headers.
- Record every distinct valid instance with exact endpoint, method, input, role, UI/API path, evidence, impact, and retest criteria.
- Keep credentials, tokens, unnecessary PII, raw Burp projects, and uncontrolled exports outside tracked files.
- Do not run denial-of-service or unbounded load testing. Keep rate-limit testing bounded and separately recorded.

## Setup helpers

`new-engagement.sh` copies the workspace and removes Git metadata from the destination. `init-engagement.sh` creates local working directories and prints the LLM-led startup sequence; neither script converts human-readable files into machine-readable state or contacts a target.
