# Task Info — Extensive Web Application Assessment

## Role

Act as an evidence-first pentesting assistant. Use the target URL, supplied credentials, supplied roles, engagement notes, Burp MCP, the current application, and the resource bank. Do not assume a fixed role model, tenant model, workflow, framework, or technology stack.

## Tooling priority

Use Burp MCP as the primary testing interface. Perform reconnaissance, sitemap and proxy-history review, request capture, replay, mutation, response comparison, API/WebSocket testing, and evidence collection through Burp MCP whenever the required operation is available there. Use a direct browser only when Burp MCP cannot expose or exercise a required rendering-dependent, browser-state, visual, or interaction-specific behavior, or when an MCP/tooling blocker is recorded. When direct browser use is necessary, record the reason, the affected workflow, and the equivalent Burp MCP coverage attempted.


## Primary objective

Perform an extensive, surface-driven web-application assessment. Find every valid instance of every applicable finding, not merely the first example. Continue until the mapped endpoints, methods, inputs, roles, workflows, and relevant protocol surfaces have been covered or an explicit blocker is recorded.

## Human inputs and LLM-led operational state

Humans primarily provide:

- `engagement/Engagement-Info.md` — target URL, Burp MCP endpoint, optional scope, browser fallback, test-data, cleanup, and free-form notes.
- `engagement/Roles-and-Credentials.md` — supplied roles, usernames, and secret references.
- `engagement/Endpoint-Notes.md` and `engagement/Input-Point-Notes.md` — optional starting notes.
- `catalogue/Finding-Catalogue.md` — reusable finding objectives.
- `resource-bank/Resource-Locator.md` and family directories — reusable and online research sources.

There is no source-to-machine conversion script. Before testing, the LLM MUST read the human-readable sources and build or update these working documents directly:

- `plans/Operational-State.md` — target, roles, sitemap state, technologies, workflows, UI/API mapping, and current scope assumptions.
- `plans/Finding-Plan.md` — the complete surface-driven list of applicable objectives and their coverage status.
- `plans/Endpoint-Inventory.md` — every discovered method/path/protocol surface.
- `plans/Input-Point-Inventory.md` — every input, source, sink, context, role, and batch.
- `plans/Resource-Review.md` — the online and local references actually read and the relevant techniques extracted.

These are LLM-maintained working state, not generated files. Update them as reconnaissance changes the understanding of the application.

## Required workflow

1. Read all human-readable engagement files, the finding catalogue, the resource-bank overview, the locator, and applicable family resources.
2. Resolve each enabled online resource that applies to the discovered technology or finding family. Extract the relevant sections, current encoding or parser variants, version/date, applicability, limitations, and source URL into `plans/Resource-Review.md`. Do not rely on a resource name alone.
3. Confirm the target URL, available credentials, supplied roles, and any optional exclusions or cleanup notes. Use the supplied role order; test every enabled role.
4. Route application traffic through the configured Burp MCP connection and review the complete sitemap and proxy history there. Perform passive reconnaissance before mutation, then update the operational state. If Burp MCP is unavailable or cannot expose a required behavior, record the blocker before using the direct browser.
5. Reconcile the Burp MCP sitemap and captured traffic with the rendered UI, browser behavior, JavaScript, route data, API calls, WebSockets, manifests, integrations, and direct routes. Direct browser use is a fallback for rendering-, browser-state-, visual-, or interaction-specific behavior, not the default testing path.
6. Compare every UI workflow with its programmatic behavior. Capture the UI request sequence through Burp MCP, replay the underlying API or WebSocket operations through Burp MCP, and compare authorization, validation, accepted fields, returned data, state changes, errors, redirects, and side effects. A UI/API behavior difference is a candidate weakness; confirm its security or business impact rather than dismissing it because the UI hides the function.
7. Build the complete finding plan from the catalogue, current technology, sitemap, UI/API map, and reviewed resources. Add discovered objectives when the surface warrants them.
8. For each finding family, map every possible input and entry point before testing: query, path, header, cookie, body, JSON, multipart, file, URL, WebSocket message, client-side source, stored field, import, export, scheduled job, and third-party boundary.
9. Test every mapped input across every reachable role in the supplied order. Continue after the first confirmed instance and record all distinct valid instances. Split work into observable batches when useful, but never use batching to omit coverage.
10. Use current, context-specific variants from the reviewed resources. For XSS, cover reflected, stored, DOM, framework, browser, encoding, Unicode, double-encoding, parser, SVG/image, multipart, content-type, and filter-context variants where applicable. For SQL injection, cover DBMS-specific syntax, case and whitespace variation, comments, encoding, parser differences, error/boolean/time behavior, and relevant request locations. Record which resource and variant informed each batch.
11. Test security headers across representative success, redirect, authentication, API, asset, error, and download responses. Check missing, weak, contradictory, inconsistent, obsolete, and deprecated headers; distinguish a deprecated header from an actual security impact. Include current expectations for CSP, HSTS, framing, referrer, permissions, MIME sniffing, and legacy headers such as `X-XSS-Protection`, `Feature-Policy`, `Expect-CT`, and HPKP where observed.
12. For every candidate, prove the control behavior, candidate behavior, impact, affected roles/objects, replay or control result, and cleanup. Do not call a boundary negative until the relevant variants and roles are covered.
13. Record every confirmed instance separately or group only genuinely identical instances with complete endpoint and input coverage. Preserve sanitized Burp evidence and enough detail for independent reproduction.

## Minimal operating constraints

The default assumption is extensive authorized testing. Do not run denial-of-service or unbounded load testing. Rate-limit testing must remain bounded and clearly separated from normal functional testing. Keep credentials, tokens, unnecessary personal data, and uncontrolled raw exports out of tracked files. For any other unusual side effect, use the engagement notes and the smallest practical test while recording the resulting state.

## Resource-bank reading rule

The resource bank is a research input, not a payload list. For every applicable enabled resource, the LLM MUST retrieve and read the source, identify the relevant sections, cross-check the details against the current target technology and context, and record the extracted references before using them. If an online source is unavailable, stale, ambiguous, or materially different from the current application, record that limitation and use a verified alternative.

## Result statuses

Use `Planned`, `In progress`, `Observed — needs confirmation`, `Confirmed finding`, `Negative for tested boundary`, `Blocked — fixture/tooling`, or `Not applicable`. `Negative for tested boundary` means the recorded boundary was actually covered; it never means “not yet checked.”

## Minimum finding record

Every candidate or confirmed finding must include the finding ID, exact role, endpoint, method, input or message, UI/API path, timestamp, precondition, expected control, sanitized evidence, observed result, affected objects or roles, reproduction steps, impact, cleanup or residual state, retest criteria, and any untested boundary.
