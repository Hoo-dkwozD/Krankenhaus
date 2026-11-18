# Engagement Inputs

> Minimal human-readable input. Complete the target, credential references, roles, and any engagement-specific notes. The LLM builds the operational state from these files, the current application, Burp MCP, and the resource bank before testing.

## Target and tooling

| Field | Value |
|---|---|
| Primary application URL | `https://EDIT_ME/` |
| Additional approved hosts or paths (optional) | `None` |
| Exclusions (optional) | `None` |
| Burp MCP endpoint | `http://127.0.0.1:9876` |
| Browser fallback notes (optional) | `Use Burp MCP by default; use the browser only when needed` |

Burp MCP is the primary interface for reconnaissance, request capture, replay, modification, sitemap review, and evidence collection. Use direct browser interaction only when Burp MCP cannot expose or exercise the required UI behavior, such as rendering-dependent flows, browser-only state, visual confirmation, or an MCP/tooling blocker. Record the reason for direct browser use in the operational state.

## Credentials and roles

Credential references belong in `Roles-and-Credentials.md`. Store passwords, tokens, and API keys only in ignored `private/` storage or a password manager.

## Test data and cleanup

| Field | Value |
|---|---|
| Test accounts or disposable data (optional) | `None` |
| Cleanup instructions (optional) | `None` |
| Application-specific notes (optional) | `None` |

## Testing defaults

This template assumes an extensive authorized web-application assessment. Test all supplied roles, endpoints, methods, inputs, workflows, and valid instances of each applicable finding. Do not run denial-of-service or unbounded load testing; rate-limit testing must remain bounded and separately identified.

## Free-form engagement notes

Add any useful context here. The field is intentionally open-ended and may be brief or detailed.
