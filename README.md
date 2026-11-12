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
- Preserve the testing workflow used in the CxC engagement: Burp MCP routing, role order, UI/API comparison, complete input mapping, automated batches, conclusive proof, cleanup, and explicit blockers.
- Make evidence usable by both a human pentester and an automation agent.

## Repository layout

```text
engagement/                  Human-readable source documents only
config/                      Generated structured scope and role metadata
catalogue/                   Human-readable finding catalogue
plans/                       Generated finding plan and machine-readable inventories
templates/                   Evidence and finding-record templates
scripts/                     Safe generation, initialization, and plan commands
evidence/                   Sanitized engagement evidence only
findings/                   Final finding records and remediation notes
private/                    Local-only credential references and sensitive notes
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
     --destination "$HOME/Documents/BDO Engagements/<Client>/<Month>/<Project>"
   ```

3. Edit only the human-readable source files:

   - `engagement/Engagement-Info.md`
   - `engagement/Roles-and-Credentials.md`
   - `engagement/Task-Info.md`
   - `engagement/Checklist.md`
   - `engagement/Endpoint-Notes.md`
   - `engagement/Input-Point-Notes.md`
   - `catalogue/Finding-Catalogue.md`

4. Store credentials outside Git. Use `Roles-and-Credentials.md` only for usernames, role labels, tenant values, and secret references. Never put passwords or tokens in tracked files.

5. Populate all generated machine-readable files:

   ```bash
   cd "$HOME/Documents/BDO Engagements/<Client>/<Month>/<Project>"
   ./scripts/build-machine-state.py
   ```

   This generates `config/*.yaml`, `config/*.csv`, `plans/*.csv`, and `plans/Finding-Plan.md`.

6. Review the generated plan and inventories before any target request. Do not hand-edit generated files; change the Markdown source and regenerate.


7. Start with passive reconnaissance and Burp MCP sitemap review. Proceed only after scope, authorization window, roles, and test boundaries are complete.

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
