```text
                       _              _                     
  /\ /\_ __ __ _ _ __ | | _____ _ __ | |__   __ _ _   _ ___ 
 / //_/ '__/ _` | '_ \| |/ / _ \ '_ \| '_ \ / _` | | | / __|
/ __ \| | | (_| | | | |   <  __/ | | | | | | (_| | |_| \__ \
\/  \/|_|  \__,_|_| |_|_|\_\___|_| |_|_| |_|\__,_|\__,_|___/
                                                            
```

# Krankenhaus

Reusable, GitHub-ready workspace for authorized web-application security engagements.

## Design goals

- Keep engagement-specific values editable in one place.
- Never commit credentials, tokens, raw PII, Burp projects, or uncontrolled exports.
- Compile a fresh finding plan from the current target, routes, roles, technologies, and scope.
- Preserve the reusable testing workflow: Burp MCP routing, role order, UI/API comparison, complete input mapping, automated batches, conclusive proof, cleanup, and explicit blockers.
- Make evidence usable by both a human pentester and an automation agent.

## Repository layout

```text
engagement/                  Human-readable web-app source documents
config/                      Generated web-app scope and role metadata
catalogue/                   Human-readable web-app finding catalogue
plans/                       Generated web-app plan and inventories
resource-bank/               Shared context bank: vulnerability-family resources, locators, and stubs
llm/                         Separate LLM-mode sources, playbooks, evidence, and generated state
templates/                   Web-app evidence and finding-record templates
scripts/                     Safe generation, initialization, and plan commands
evidence/                    Sanitized web-app engagement evidence
findings/                    Web-app finding records and remediation notes
private/                     Local-only credential references and sensitive notes
```

## New engagement workflow

1. Clone this repository as a template; do not test a target during setup.

   ```bash
   git clone <template-repository-url> <template-clone>
   cd <template-clone>
   ```

2. Create a detached project copy. The source clone remains reusable and the destination contains no `.git` directory:

   ```bash
   ./scripts/new-engagement.sh \
     --destination "$HOME/Documents/Security Engagements/<Client>/<Period>/<Project>"
   ```

3. Edit only the human-readable source files for the applicable mode:

   **Web-application mode**

   - `engagement/Engagement-Info.md`
   - `engagement/Roles-and-Credentials.md`
   - `engagement/Task-Info.md`
   - `engagement/Checklist.md`
   - `engagement/Endpoint-Notes.md`
   - `engagement/Input-Point-Notes.md`
   - `catalogue/Finding-Catalogue.md`
   - `resource-bank/Resource-Locator.md` and applicable family resources

   **LLM testing mode**

   - `llm/engagement/LLM-Engagement-Info.md`
   - `llm/engagement/LLM-Target-Context.md`
   - `llm/engagement/LLM-Policy-Matrix.md`
   - `llm/engagement/LLM-Testing-Plan.md`
   - `llm/playbooks/` reviewed playbooks and integrations

4. Store credentials outside Git. Use `Roles-and-Credentials.md` only for usernames, role labels, tenant values, and secret references. Never put passwords or tokens in tracked files.

5. Build the machine-readable state:

   ```bash
   ./scripts/build-machine-state.py
   ./scripts/build-llm-state.py
   ```

   Run the command for each active mode. The first generates web-app state; the second generates separate LLM-mode state under `llm/generated/`.

6. Review the generated plans and inventories before any target request. Do not hand-edit generated files; change the Markdown source and regenerate.

7. Load the applicable context bank and playbook references before testing:

   - Web application: read `resource-bank/README.md`, `resource-bank/Resource-Locator.md`, and the relevant vulnerability-family directory after the current surface is mapped. Record the resource IDs, versions, provenance, and applicability used for each finding family.
   - LLM testing: read `llm/playbooks/Playbook-Index.md` and the selected integration under `llm/playbooks/` after the target context and policy matrix are complete. A playbook reference guides approved testing; it does not activate a campaign or authorize a payload by itself.

8. Start with passive reconnaissance and Burp MCP sitemap review. Proceed only after scope, authorization window, roles, test boundaries, and the selected context/playbook references are complete.

9. Before each finding family or LLM campaign, re-check the selected resource/playbook version and engagement-specific exclusions. Do not send every resource-bank payload or technique automatically.

## Evidence rules

- Route all target HTTP traffic through Burp MCP when the engagement task requires it.
- Test roles independently in this order: **Super Admin → Admin → Supervisor → Agent**.
- Do not generalize one role, tenant, object, or endpoint result to another.
- Record exact method, path, role, tenant, status, sanitized request/response evidence, and timestamp.
- For a finding, prove: precondition → control behavior → candidate action → postcondition → replay/control result → cleanup.
- Do not classify an untested browser, WebSocket, mutation, cross-tenant, file-upload, or external-side-effect boundary as negative.
- Use low-impact canaries. Avoid destructive actions, real email/webhooks, broad extraction, lockouts, password changes, passkey enrollment, OOB callbacks, or third-party actions unless separately approved.

## Safety

`new-engagement.sh` copies files and removes Git metadata only from the new destination. It does not contact a target, delete the source clone, or modify credentials. Review the generated destination before use.
