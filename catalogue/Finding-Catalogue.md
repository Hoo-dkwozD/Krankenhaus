# Baseline Finding Catalogue

This is a catalogue of test objectives, not a list of findings. `scripts/build-finding-plan.py` compiles the active plan from this file for each engagement. Add, disable, or annotate entries based on the actual sitemap, technologies, role model, and authorization.

Priority is a default planning value: P0 = critical/high impact, P1 = high, P2 = medium, P3 = low/informational. Replace it after evidence.

## Information disclosure, configuration, and deployment

### CXC-INF-01 — Banner and technology disclosure
- Default priority: P3
- Surface: public headers, HTML, assets, manifests, error pages

### CXC-INF-02 — Default files and administrative defaults
- Default priority: P2
- Surface: public resources, framework files, health/debug/admin paths

### CXC-INF-03 — Exposed files, backups, source maps, and build artifacts
- Default priority: P1
- Surface: asset graph, source maps, backups, VCS/deployment files

### CXC-INF-04 — Web metafile and crawler leakage
- Default priority: P3
- Surface: robots.txt, sitemap.xml, security.txt, manifest

### CXC-INF-05 — Application and architecture mapping gaps
- Default priority: P2
- Surface: Burp sitemap, JavaScript, route data, API versions, integrations

### CXC-INF-06 — Information exposure through HTML, JavaScript, comments, and client configuration
- Default priority: P2
- Surface: HTML comments, chunks, route modules, configuration

### CXC-INF-07 — Verbose errors, stack traces, debug modes, and correlation leakage
- Default priority: P2
- Surface: malformed requests, API errors, route errors, telemetry

### CXC-INF-08 — TLS certificate, protocol, and transport weakness
- Default priority: P1
- Surface: HTTPS, redirects, approved subdomains, integrations

### CXC-INF-09 — Deprecated, missing, or contradictory security headers
- Default priority: P3
- Surface: HTML, API, error, asset, authentication responses

### CXC-INF-10 — HSTS not enforced or inconsistently scoped
- Default priority: P2
- Surface: HTTPS and redirect behavior

### CXC-INF-11 — CSP absent, weak, bypassable, or inconsistent
- Default priority: P2
- Surface: HTML, API/error pages, CSP reports, rendered resources

### CXC-INF-12 — Clickjacking and framing policy weakness
- Default priority: P2
- Surface: login, cases, admin, reports, profile, tenant/workflow pages

### CXC-INF-13 — Cache poisoning, cache deception, and sensitive caching
- Default priority: P1
- Surface: CDN/proxy, HTML, API, route data, reports, dashboards

## Identity, authentication, sessions, and credentials

### CXC-AUTH-01 — Username or account enumeration
- Default priority: P2
- Surface: login, recovery, verification, passkey, directory, email

### CXC-AUTH-02 — Weak password policy and password quality enforcement
- Default priority: P1
- Surface: login, password change, expiry, tenant settings

### CXC-AUTH-03 — Password autocomplete and credential exposure in browser behavior
- Default priority: P3
- Surface: login, reset/change, passkey, browser storage

### CXC-AUTH-04 — Missing brute-force protection, rate-limit bypass, and credential-stuffing resistance
- Default priority: P1
- Surface: login, 2FA, passkey, recovery, verification

### CXC-AUTH-05 — Account lockout and recovery abuse
- Default priority: P1
- Surface: recovery, expired-password, verification, support/admin recovery

### CXC-AUTH-06 — Missing, optional, or bypassable MFA/2FA and passkey controls
- Default priority: P1
- Surface: login, 2FA, passkey, tenant settings, recovery

### CXC-AUTH-07 — Authentication flow confusion and step skipping
- Default priority: P1
- Surface: CSRF, login, verify, 2FA, tenant selection, passkey

### CXC-AUTH-08 — Session fixation and token issuance weakness
- Default priority: P1
- Surface: authentication cookies, login, tenant selection, WebSocket

### CXC-AUTH-09 — JWT and token claim trust failures
- Default priority: P0
- Surface: token cookies, API authorization, tenant switching, WebSocket

### CXC-AUTH-10 — Cookie attribute and scope weakness
- Default priority: P2
- Surface: session/CSRF/tenant cookies, integrations

### CXC-AUTH-11 — Excessive session timeout, idle timeout, or failed revocation
- Default priority: P1
- Surface: session, verify, logout, password change, WebSocket

### CXC-AUTH-12 — Concurrent sessions and device/session management weakness
- Default priority: P3
- Surface: login, profile, logout, password change, tenant selection

### CXC-AUTH-13 — Broken logout
- Default priority: P1
- Surface: logout, browser session, API, WebSocket

### CXC-AUTH-14 — Session hijacking and token exposure
- Default priority: P0
- Surface: URLs, referrers, logs, HTML, storage, integrations, WebSocket

### CXC-AUTH-15 — OAuth, external identity, and passkey binding flaws
- Default priority: P1
- Surface: OAuth/SSO, passkey, external identity/call integrations

## Authorization, access control, and multi-tenancy

### CXC-AC-01 — Broken vertical access control / BFLA
- Default priority: P0
- Surface: every API family, admin, reports, logs, jobs, settings

### CXC-AC-02 — Broken horizontal access control / BOLA / IDOR
- Default priority: P0
- Surface: case, email, user, report, schedule, task, notification, queue, voice IDs

### CXC-AC-03 — Tenant isolation failure
- Default priority: P0
- Surface: tenant picker/switch, settings, cases, email, reports, dashboards, WebSocket

### CXC-AC-04 — UI/API permission mismatch
- Default priority: P1
- Surface: hidden buttons, permissions, cases, users, KB, reports, email, tasks

### CXC-AC-05 — Unprotected or hidden routes
- Default priority: P1
- Surface: direct UI routes, route data, admin/config/schedule/supervisor APIs

### CXC-AC-06 — Excessive data exposure
- Default priority: P1
- Surface: cases, email, users, dashboards, reports, logs, audit, agent data

### CXC-AC-07 — Mass assignment and property-level authorization
- Default priority: P1
- Surface: case, user, team, task, email, KB, tenant, settings mutations

### CXC-AC-08 — Report/export authorization and data leakage
- Default priority: P1
- Surface: catalogue, report packs/keys, exports, asynchronous downloads

### CXC-AC-09 — Authorization through alternate methods or content types
- Default priority: P1
- Surface: all APIs, especially admin, cases, reports, authentication

## Session integrity, CSRF, CORS, and browser controls

### CXC-WEB-01 — CSRF protection failure
- Default priority: P1
- Surface: state-changing authentication, tenant, case, user, task, email, settings, admin APIs

### CXC-WEB-02 — CORS policy weakness
- Default priority: P2
- Surface: API/preflight, login, integrations

### CXC-WEB-03 — Tabnabbing and reverse-tabnabbing
- Default priority: P3
- Surface: external links, email, reports, KB, notifications, integrations

### CXC-WEB-04 — Open redirect and unsafe redirect parameters
- Default priority: P2
- Surface: login, logout, recovery, tenant, integrations

### CXC-WEB-05 — Host header injection and password-reset poisoning
- Default priority: P1
- Surface: redirects, recovery URLs, email generation, proxy boundary

### CXC-WEB-06 — Sensitive data in URLs, referrers, or browser history
- Default priority: P2
- Surface: query strings, redirects, route data, third-party requests

### CXC-WEB-07 — Browser storage and offline/PWA leakage
- Default priority: P1
- Surface: storage, IndexedDB, service worker, offline pages, push

### CXC-WEB-08 — WebSocket authorization and tenant isolation
- Default priority: P0
- Surface: WebSocket, chat, voice, notifications

### CXC-WEB-09 — WebRTC/call integration boundary weakness
- Default priority: P1
- Surface: voice, Amazon Connect, WebRTC, PWA permissions

## Input validation and server-side injection

### CXC-INJ-01 — Reflected, stored, and DOM-based XSS
- Default priority: P1
- Surface: cases, email, notifications, searches, KB, reports, logs, Svelte sinks

### CXC-INJ-02 — SQL injection
- Default priority: P0
- Surface: search, sort/filter, pagination, reports, analytics, logs, dashboards

### CXC-INJ-03 — NoSQL injection
- Default priority: P0
- Surface: JSON APIs, selectors, search/filter, login, cases, reports

### CXC-INJ-04 — Server-side template injection
- Default priority: P0
- Surface: email, reports, notifications, KB, macros, templates

### CXC-INJ-05 — OS command injection
- Default priority: P0
- Surface: reports, uploads, conversion, exports, jobs, diagnostics

### CXC-INJ-06 — Path traversal and file inclusion
- Default priority: P0
- Surface: downloads, report keys, attachments, templates, static resources

### CXC-INJ-07 — Unrestricted or unsafe file upload
- Default priority: P1
- Surface: cases, profile, KB, email, reports, attachments, admin tools

### CXC-INJ-08 — Server-side request forgery
- Default priority: P0
- Surface: URL imports, webhooks, previews, reports, images, integrations

### CXC-INJ-09 — XML external entity and unsafe XML processing
- Default priority: P0
- Surface: XML/SVG/SOAP/import/report/file processing

### CXC-INJ-10 — Insecure deserialization
- Default priority: P0
- Surface: cookies, sessions, jobs, queues, reports, WebSocket/API bodies

### CXC-INJ-11 — Prototype pollution and parameter pollution
- Default priority: P1
- Surface: JSON merge, search/filter, settings, saved searches, task/report config

### CXC-INJ-12 — CRLF/header injection and response splitting
- Default priority: P1
- Surface: redirects, cookies, downloads, email, filenames, logging

### CXC-INJ-13 — HTTP request smuggling and proxy desynchronization
- Default priority: P0
- Surface: reverse proxy, HTTP/2-to-HTTP/1 translation, connection reuse

### CXC-INJ-14 — GraphQL-specific weaknesses
- Default priority: P1
- Surface: GraphQL endpoint if discovered

## Business logic, resource controls, and workflow abuse

### CXC-BIZ-01 — Workflow step bypass
- Default priority: P1
- Surface: cases, email approval, reports, jobs, authentication, tasks

### CXC-BIZ-02 — Unauthorized state transition or privilege modification
- Default priority: P0
- Surface: case/user/task/email/settings/admin mutations

### CXC-BIZ-03 — Race conditions and double-spend behavior
- Default priority: P1
- Surface: cases, email, tasks, reports, authentication, notifications

### CXC-BIZ-04 — Unrestricted resource consumption
- Default priority: P1
- Surface: cases, reports, analytics, logs, notifications, uploads, WebSocket

### CXC-BIZ-05 — Rate-limit and quota inconsistency
- Default priority: P1
- Surface: auth, recovery, APIs, reports, search, WebSocket, uploads

### CXC-BIZ-06 — Client-side trust and hidden-field tampering
- Default priority: P1
- Surface: forms, JSON, query values, local storage, route data

### CXC-BIZ-07 — Notification, read-state, and audit integrity
- Default priority: P1
- Surface: notifications, badges, briefing, audit, WebSocket

### CXC-BIZ-08 — Email and outbound communication abuse
- Default priority: P1
- Surface: outbound email, email APIs, cases, notifications

### CXC-BIZ-09 — Report, export, and scheduled-job abuse
- Default priority: P1
- Surface: reports, jobs, monitoring, analytics

## Client-side and modern browser findings

### CXC-CLIENT-01 — DOM XSS and unsafe client sinks
- Default priority: P1
- Surface: Svelte chunks, cases, email, reports, KB, notifications

### CXC-CLIENT-02 — PostMessage and cross-window trust
- Default priority: P1
- Surface: CCP/WebRTC, embedded panels, popups, auth/passkey

### CXC-CLIENT-03 — Third-party script and supply-chain exposure
- Default priority: P1
- Surface: CSP, HTML, CDN, Sentry, Cloudflare, Amazon Connect

### CXC-CLIENT-04 — Outdated third-party libraries and software
- Default priority: P2
- Surface: assets, headers, build metadata, dependency evidence

### CXC-CLIENT-05 — Service worker, cache, and push-notification privacy
- Default priority: P1
- Surface: PWA, service worker, notifications, dashboard, cases

## API-specific and protocol findings

### CXC-API-01 — API inventory and method inconsistency
- Default priority: P1
- Surface: undocumented routes, query shapes, methods, loaders

### CXC-API-02 — Object-level authorization (BOLA/IDOR)
- Default priority: P0
- Surface: all object/list APIs

### CXC-API-03 — Function-level authorization (BFLA)
- Default priority: P0
- Surface: admin, reports, logs, monitoring, settings, management APIs

### CXC-API-04 — Excessive data exposure and field-level authorization
- Default priority: P1
- Surface: cases, users, emails, dashboards, reports, logs, audit

### CXC-API-05 — Mass assignment and unsafe object binding
- Default priority: P1
- Surface: users, cases, tasks, email, settings, KB, reports

### CXC-API-06 — Pagination, filtering, sorting, and query abuse
- Default priority: P1
- Surface: cases, email, notifications, logs, audit, users, reports

### CXC-API-07 — API rate limiting and resource control
- Default priority: P1
- Surface: auth, search, reports, analytics, logs, WebSocket, uploads

### CXC-API-08 — Content-type, parser, and protocol confusion
- Default priority: P1
- Surface: auth, APIs, uploads, WebSocket upgrade, proxy

### CXC-API-09 — GraphQL, OAuth, JWT, and API-key-specific controls
- Default priority: P0
- Surface: only if the technology is exposed

## Logging, monitoring, and operational security

### CXC-MON-01 — Log injection and log forging
- Default priority: P1
- Surface: client-error, user-action, app logs, audit, case/email fields

### CXC-MON-02 — Sensitive data in logs, errors, monitoring, or telemetry
- Default priority: P1
- Surface: logs, audit, Sentry, client errors, telemetry

### CXC-MON-03 — Audit trail integrity and completeness
- Default priority: P1
- Surface: audit logs, auth, tenant, privilege, user-action events

### CXC-MON-04 — Monitoring/admin endpoint exposure
- Default priority: P1
- Surface: monitoring jobs, operations, readiness, health, logs, admin UI
