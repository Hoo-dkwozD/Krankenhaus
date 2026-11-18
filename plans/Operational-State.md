# Operational State

> LLM-maintained working document. Build this from the human-readable engagement files, current target surface, Burp MCP sitemap/history, browser/UI behavior, and resource review before testing. Update it continuously; no conversion script is used.

## Target, tooling, and roles

- Primary URL: `EDIT_ME`
- Additional in-scope hosts/paths: `None`
- Exclusions: `None`
- Burp MCP endpoint: `http://127.0.0.1:9876`
- Browser fallback notes: `Use Burp MCP by default; use the browser only when needed`
- Role order and credential references: see `engagement/Roles-and-Credentials.md`
- Tooling decision: Burp MCP is primary; record the reason and attempted MCP coverage whenever direct browser use is needed.

## Engagement interpretation

- Assessment mode: extensive web application testing
- Test-data and cleanup notes: `EDIT_ME`
- Current scope assumptions: `EDIT_ME`
- DDoS/load testing: excluded unless separately directed
- Rate-limit testing: bounded and separately recorded

## Reconnaissance state

- Engagement started/evidence found: `EDIT_ME`
- Sitemap reviewed: `EDIT_ME`
- UI routes reviewed: `EDIT_ME`
- API/WebSocket routes reviewed: `EDIT_ME`
- Technologies and frameworks: `EDIT_ME`
- Authentication and session model: `EDIT_ME`
- Roles and authorization model: `EDIT_ME`
- Tenant/organization model, if any: `EDIT_ME`
- Data and workflow model: `EDIT_ME`

## UI/API comparison

Record each meaningful UI-to-programmatic difference, including authorization, validation, fields, response data, errors, redirects, state transitions, and side effects.

| Comparison ID | UI workflow | UI request sequence | API/WebSocket operation | Difference observed | Security/business impact | Status | Evidence |
|---|---|---|---|---|---|---|---|
| UIAPI-0001 | `EDIT_ME` | `EDIT_ME` | `EDIT_ME` | `EDIT_ME` | `EDIT_ME` | Planned |  |

## Coverage summary

- Finding objectives applicable: `EDIT_ME`
- Endpoints/methods/protocols mapped: `EDIT_ME`
- Input points mapped: `EDIT_ME`
- Roles tested: `EDIT_ME`
- Distinct valid instances found: `EDIT_ME`
- Remaining untested boundaries: `EDIT_ME`
- Latest update: `EDIT_ME`
