# Extensive Web Application Assessment Checklist

Use this as a practical coverage gate. It is intentionally short on configuration and broad on testing. The LLM maintains the working state in `plans/` directly; no conversion script is required.

## Start

- [ ] Read `engagement/Engagement-Info.md`, `engagement/Roles-and-Credentials.md`, `engagement/Task-Info.md`, and any supplied notes.
- [ ] Confirm the target URL, credential references, supplied roles, optional exclusions, and optional cleanup notes.
- [ ] Confirm the Burp MCP endpoint; default: `http://127.0.0.1:9876`.
- [ ] Read `resource-bank/README.md`, `resource-bank/Resource-Locator.md`, and the applicable family resources.
- [ ] Resolve enabled online references and record the relevant sections, versions/dates, techniques, limitations, and applicability in `plans/Resource-Review.md`.
- [ ] Build or refresh `plans/Operational-State.md`, `plans/Finding-Plan.md`, `plans/Endpoint-Inventory.md`, and `plans/Input-Point-Inventory.md` before testing.

## Reconnaissance and application mapping

- [ ] Use Burp MCP as the primary interface for the complete sitemap, proxy history, request capture, replay, mutation, and evidence.
- [ ] Review public resources, redirects, certificates, headers, robots, manifests, service workers, build metadata, JavaScript, route data, API strings, WebSockets, and integrations through Burp MCP where available.
- [ ] Record every UI route, direct route, API-only route, feature-gated route, legacy route, discovered method, WebSocket surface, upload, import, export, scheduled job, and third-party boundary.
- [ ] Map each visible UI workflow to its underlying API or WebSocket requests through Burp MCP.
- [ ] Replay UI-backed operations programmatically through Burp MCP and compare authorization, validation, fields, responses, errors, state changes, and side effects. Use the direct browser only for a recorded MCP/tooling, rendering, browser-state, visual, or interaction-specific gap.
- [ ] Treat meaningful UI/API behavioral differences as candidate weaknesses and test their security or business impact.
- [ ] Record every supplied role in the order defined by the engagement, without assuming fixed role names.

## Exhaustive finding coverage

- [ ] Reconcile the finding catalogue with the current technologies and mapped surface.
- [ ] For every applicable finding family, map all inputs: query, path, header, cookie, body, JSON, multipart, file, URL, stored value, import, export, WebSocket message, client-side source, and third-party boundary.
- [ ] Test every mapped input for every reachable role.
- [ ] Continue after the first finding and record every distinct valid instance.
- [ ] Use batches only for observability; do not use batching to reduce coverage.
- [ ] Record the exact resource reference and technique variant used for each relevant test batch.
- [ ] Do not mark a boundary negative until its role, method, input, context, protocol, and relevant variants were covered.

## Current input and parser variants

- [ ] For XSS, cover reflected, stored, and DOM contexts plus framework, browser, encoding, Unicode, double-encoding, parser, SVG/image, multipart, content-type, and filter-context variants where applicable.
- [ ] For SQL injection, cover DBMS-specific syntax, case, whitespace, comments, encoding, parser differences, error, boolean, time, and request-location variants where applicable.
- [ ] Apply current resource-bank references rather than relying on remembered or static payloads.
- [ ] Test file uploads, XML/SVG, deserialization, command, template, path, URL-fetch, prototype/parameter, CRLF, request-smuggling, and GraphQL inputs when the surface exposes them.

## Headers and baseline controls

- [ ] Check security headers on normal HTML, authenticated pages, APIs, assets, redirects, errors, downloads, and alternate hosts.
- [ ] Check missing, weak, contradictory, inconsistent, obsolete, and deprecated headers.
- [ ] Evaluate current expectations for CSP, HSTS, framing, referrer, permissions, MIME sniffing, and legacy headers such as `X-XSS-Protection`, `Feature-Policy`, `Expect-CT`, and HPKP when observed.
- [ ] Distinguish an obsolete header from a security impact and record the affected response classes.
- [ ] Check default files, source maps, verbose errors, debug behavior, caching, TLS, metadata, and technology disclosure.

## Roles, authorization, and workflows

- [ ] Test vertical and horizontal access control for every supplied role.
- [ ] Test object, field, function, export, report, workflow-step, and state-transition authorization.
- [ ] Compare UI permissions with direct API and WebSocket permissions.
- [ ] Test alternate methods, content types, duplicate parameters, path normalization, hidden fields, and direct object references.
- [ ] Test tenant or organizational boundaries when the application has them; do not require tenant data when it does not.
- [ ] Test authentication, sessions, CSRF, CORS, browser storage, WebSockets, realtime, and integrations where discovered.

## Completion and evidence

- [ ] Record every candidate and confirmed instance with role, endpoint, method, input, UI/API path, timestamp, and Burp evidence.
- [ ] Include control behavior, candidate behavior, impact, replay/control result, cleanup or residual state, and retest criteria.
- [ ] Keep credentials, tokens, unnecessary PII, raw sensitive exports, and Burp projects outside tracked files.
- [ ] Record all blockers and untested boundaries explicitly.
- [ ] Confirm the sitemap, operational state, finding plan, endpoint inventory, input inventory, resource review, and findings are current.

## Explicit exception

- [ ] No denial-of-service or unbounded load testing was run.
- [ ] Rate-limit testing was bounded and separately recorded.
