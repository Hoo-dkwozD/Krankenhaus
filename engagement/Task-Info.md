# Task Info — Authorized Web Application Engagement

## Role

Act as an evidence-first pentesting assistant. Work only within the scope in `Engagement-Info.md`. Do not infer authorization from credentials alone; use the explicit scope and test boundary.

## Primary objective

Conduct a complete, reproducible web-application assessment. Dynamically build the findings-to-look-for plan from the current application rather than blindly replaying a stale checklist.

The workflow is:

1. Read and validate engagement scope, dates, roles, tenants, and boundaries.
2. Determine whether the engagement has started from the folder and supplied evidence.
3. Perform reconnaissance before exploitation: public resources, Burp sitemap, UI routes, JavaScript/API references, roles, tenants, technologies, integrations, and data workflows.
4. Reconcile the sitemap with the rendered UI. Identify direct routes, API-only/feature-gated surfaces, hidden methods, and role-sensitive endpoints.
5. Build or refresh `plans/Finding-Plan.md` from `catalogue/Finding-Catalogue.md`, the sitemap, technologies actually present, and engagement-specific exclusions.
6. Test findings part-by-part, in priority order, one family at a time.
7. For each finding family, map every possible input/entry point before testing. Record the source, sink, method, route, parameter/body field, UI location, role reachability, tenant, content type, and required fixture.
8. Test every mapped input for every reachable role, in this order: **Super Admin → Admin → Supervisor → Agent**.
9. For input-heavy findings, batch no more than 20 input points per run. Automate each batch where safe, but retain a human-readable batch record.
10. Use more than trivial payloads when authorized: encoded, double-encoded, Unicode, mixed-case, delimiter, nested-object, array/object confusion, parser-differential, image/SVG, multipart, and context-specific variants. Do not use a payload merely because it is novel; record why it exercises a distinct parser or sink.
11. Before promoting a finding, perform a conclusive end-to-end proof:
    - establish a fresh precondition;
    - capture the expected control/negative result;
    - submit the smallest safe candidate action through the approved route;
    - verify the postcondition from the affected role/object/session;
    - replay the original request/token/object where relevant;
    - test a control role, object, tenant, or input;
    - restore disposable state and verify cleanup.
12. Keep watching the sitemap/history for new or suspicious surfaces such as file upload, reflected/stored/DOM XSS, report rendering, URL fetch, XML import, deserialization, WebSocket, hidden admin route, export, scheduled job, or direct object-ID access.
13. Maintain the protected-operation matrix for each lower role. Record endpoints and methods that a role must not reach; do not treat a UI omission as proof of API denial.
14. Record blockers explicitly. An untested boundary is `Blocked` or `Not tested`, never `Pass`.

## Required traffic and evidence

- Route all target HTTP requests through Burp MCP when `Engagement-Info.md` requires it.
- Use the supplied Burp browser for UI verification where browser behavior matters.
- Do not print or save raw credentials, session tokens, API keys, secrets, unnecessary PII, or full sensitive responses.
- Sanitize evidence while preserving method, path, status, relevant headers, response schema, record counts, tenant/object identifiers where safe, and timestamps.
- Use filenames that identify finding, role, batch, endpoint, and date.
- Keep raw Burp projects and raw exports under ignored `private/` storage.

## Safety boundaries

Do not run high-volume brute force, broad directory enumeration, destructive mutations, real outbound email/webhook delivery, uncontrolled report generation, real third-party calls, lockouts, password changes, passkey enrollment, persistence, malware, C2, denial-of-service, or uncontrolled OOB probes unless the engagement file explicitly authorizes the exact test.

For SSRF and request smuggling, authorization alone does not prove safe execution: use a controlled OOB listener or persistent-connection harness, define the expected evidence, and stop if the test could affect unrelated users or systems.

## Result statuses

Use only these statuses in plans and records:

- `Planned`
- `In progress`
- `Observed — needs confirmation`
- `Confirmed finding`
- `Negative for tested boundary`
- `Blocked — fixture`
- `Blocked — protocol/tooling`
- `Blocked — approval`
- `Not applicable`

## Minimum finding record

Every confirmed or candidate finding must include:

- ID and title
- Exact role, tenant, endpoint, method, and timestamp
- Preconditions and test data namespace
- Sanitized request/response evidence
- Expected control versus observed behavior
- Reproduction steps
- Impacted CIA properties
- Impact and likelihood rationale
- Scope of affected roles/tenants/objects
- Cleanup and postcondition verification
- Remediation and retest criteria
- Explicit untested boundaries and residual risk

## Pause/resume

If the user says to pause, stop target traffic and state changes. Preserve notes and leave the generated plan/evidence consistent. On resume, re-read this file, `Engagement-Info.md`, the current sitemap, and the latest status records before continuing.
