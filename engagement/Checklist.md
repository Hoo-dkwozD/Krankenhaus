# Engagement Checklist

Use this checklist as the human execution gate. Select the web-app and/or separate LLM workstream. The active web-app finding list is generated in `plans/Finding-Plan.md`; the active LLM objective list is generated in `llm/generated/LLM-Finding-Plan.md`.

## Before testing

- [ ] Read `engagement/Engagement-Info.md`.
- [ ] Read `engagement/Task-Info.md`.
- [ ] Confirm written authorization, dates, hosts, ports, and exclusions.
- [ ] Confirm Burp MCP endpoint and browser availability.
- [ ] Confirm credential references without copying secrets into tracked files.
- [ ] Confirm roles and test order: Super Admin → Admin → Supervisor → Agent.
- [ ] Confirm tenant model and approved disposable-fixture namespace.
- [ ] Confirm approvals for mutations, uploads, SSRF/OOB, WebSocket frames, request smuggling, recovery/lockout, email/webhooks, third-party integrations, and concurrency.
- [ ] Generate `plans/Finding-Plan.md`.
- [ ] Create or refresh the endpoint and protected-operation inventories.
- [ ] Read `resource-bank/README.md` and `resource-bank/Resource-Locator.md`; after surface mapping, select applicable family resources and record IDs, versions, provenance, and exclusions.

## Mode selection and LLM testing

- [ ] Select web-application mode, LLM testing mode, or both as separate workstreams.
- [ ] If LLM mode is active, read `llm/README.md` and `llm/engagement/LLM-Source-of-Truth.md`.
- [ ] Complete LLM business/user context, audience, age/vulnerability, jurisdiction, language, workflow, policy, and escalation fields.
- [ ] Specify every LLM target's exact endpoint, method, authentication reference, prompt insertion path, response extraction path, streaming/multi-turn behavior, and reset procedure.
- [ ] Record target model/provider/version, system-prompt visibility, guardrails, filters, memory, tools, RAG, rendering, and production parameters.
- [ ] Complete and approve the LLM policy matrix, hard exclusions, proxy-only objectives, budget, rate, turn, reproduction, evidence, and human-review controls.
- [ ] Run `scripts/build-llm-state.py`; do not edit `llm/generated/` directly.
- [ ] Keep LLM prompts, responses, scores, campaigns, and findings separate from web-app evidence and findings.
- [ ] Read `llm/playbooks/Playbook-Index.md` and the selected playbook integration; treat the playbook as a controlled reference, not automatic authorization or activation.

## Reconnaissance and UI/API comparison

- [ ] Public resources, headers, certificates, redirects, robots, security.txt, manifest, service worker, and version/build metadata.
- [ ] Burp MCP sitemap and proxy history reviewed.
- [ ] JavaScript, route chunks, API strings, SvelteKit data loaders, WebSocket, and integration references reviewed.
- [ ] Visible UI routes recorded for each role.
- [ ] Direct routes absent from navigation tested separately.
- [ ] API-backed UI workflows mapped.
- [ ] API-only, feature-gated, legacy, and discovered-only endpoints classified.
- [ ] Protected endpoint matrix updated for each lower role.
- [ ] Data workflows mapped from the end-user UI perspective.
- [ ] Context-bank resources and selected LLM playbook references are recorded for the surfaces and finding families that will be tested.

## Baseline information and configuration controls

- [ ] Banner and technology disclosure.
- [ ] Default files and administrative defaults.
- [ ] Exposed files, backups, source maps, and build artifacts.
- [ ] Web metafile and crawler leakage.
- [ ] HTML/JavaScript comments and client configuration.
- [ ] Error verbosity, stack traces, debug modes, and correlation leakage.
- [ ] TLS certificate, protocol, cipher, and transport configuration.
- [ ] Security headers, HSTS, CSP, framing, referrer, and permissions policy.
- [ ] Cache-control, cache-key, cache deception, and sensitive caching behavior.

## Authentication and session controls

- [ ] Account enumeration.
- [ ] Password policy and password quality enforcement.
- [ ] Password autocomplete and browser credential behavior.
- [ ] Brute-force protection and rate-limit boundaries using only approved low-volume sequences.
- [ ] Account lockout and recovery abuse.
- [ ] MFA/2FA and passkey enforcement/binding.
- [ ] Authentication step skipping and flow confusion.
- [ ] Session fixation and token issuance.
- [ ] JWT/token claim trust and revocation.
- [ ] Cookie attributes and scope.
- [ ] Idle timeout, absolute timeout, password-change revocation, and logout revocation.
- [ ] Concurrent sessions and device/session management.
- [ ] Token exposure in URLs, storage, referrers, logs, telemetry, and WebSocket boundaries.
- [ ] OAuth/SSO/passkey binding if discovered.

## Broken Access Control, Authorization, and Tenancy

- [ ] Broken Access Control / vertical access control / BFLA.
- [ ] Broken Access Control / horizontal access control / BOLA / IDOR.
- [ ] Tenant isolation and tenant-switch boundaries.
- [ ] UI/API permission mismatch.
- [ ] Hidden and unprotected routes.
- [ ] Excessive data exposure and field-level authorization.
- [ ] Mass assignment and property-level authorization.
- [ ] Report/export authorization.
- [ ] Alternate methods, content types, duplicate parameters, and path normalization.
- [ ] Owner, non-owner, team, and cross-tenant object fixtures tested where available.

## Browser, CSRF, CORS, and realtime

- [ ] CSRF on every approved state-changing family.
- [ ] CORS origin, credentials, preflight, null-origin, and subdomain behavior.
- [ ] Tabnabbing and reverse-tabnabbing.
- [ ] Open redirects and unsafe redirect parameters.
- [ ] Host-header and forwarded-host behavior, including recovery links.
- [ ] Sensitive data in URLs, referrers, and browser history.
- [ ] Browser storage, offline, service-worker, cache, and push behavior.
- [ ] WebSocket handshake, token, origin, subscription, message, replay, and tenant authorization.
- [ ] WebRTC/CCP/third-party integration boundaries.

## Input and injection testing

- [ ] Map every input point before testing each finding family.
- [ ] Test all reachable roles in the required order.
- [ ] Batch no more than 20 mapped inputs per automated run.
- [ ] Record input source, sink, content type, context, fixture, role, tenant, and batch.
- [ ] Reflected, stored, and DOM XSS.
- [ ] SQL and NoSQL injection.
- [ ] Server-side template injection.
- [ ] OS command injection.
- [ ] Path traversal and file inclusion.
- [ ] File upload and attachment processing.
- [ ] SSRF with controlled OOB evidence where approved.
- [ ] XML/XXE and unsafe XML/SVG processing.
- [ ] Insecure deserialization.
- [ ] Prototype/parameter pollution.
- [ ] CRLF/header injection.
- [ ] HTTP request smuggling/desynchronization with a persistent-connection harness.
- [ ] GraphQL, OAuth, JWT, or API-key controls only if discovered.

## API, business logic, and resource controls

- [ ] API inventory and method inconsistency.
- [ ] Object-level and function-level authorization.
- [ ] Field-level exposure and unsafe binding.
- [ ] Pagination, filtering, sorting, count, and page-size limits.
- [ ] Rate limits and resource controls.
- [ ] Parser and content-type confusion.
- [ ] Workflow-step bypass.
- [ ] Unauthorized state transitions or privilege changes.
- [ ] Replay, duplicate submission, and bounded concurrency.
- [ ] Client-side hidden-field tampering.
- [ ] Notification/read-state/audit integrity.
- [ ] Email and outbound communication abuse.
- [ ] Report, export, scheduled-job, and webhook abuse.

## Client and monitoring controls

- [ ] DOM XSS and unsafe client sinks.
- [ ] postMessage/cross-window origin validation.
- [ ] Third-party scripts, supply chain, SRI, and permissions.
- [ ] Outdated libraries/software where exploitable evidence exists.
- [ ] Service-worker/cache/push privacy.
- [ ] Log injection and log forging.
- [ ] Sensitive data in logs, errors, monitoring, or telemetry.
- [ ] Audit-trail integrity and completeness after known events.
- [ ] Monitoring/admin endpoint exposure.

## Evidence and closure

- [ ] Every candidate has exact role, tenant, method, path, timestamp, and Burp evidence reference.
- [ ] Every promoted finding has precondition, expected control, action, postcondition, replay/control result, and cleanup verification.
- [ ] Candidates are separated from confirmed findings.
- [ ] Browser, WebSocket, mutation, fixture, protocol, and approval blockers are explicit.
- [ ] Disposable state is restored and verified.
- [ ] Raw secrets, tokens, PII, and Burp projects remain outside Git.
- [ ] `findings/` records are complete enough for independent reproduction.
- [ ] Final sitemap, endpoint inventory, input inventory, protected matrix, and finding plan are current.
