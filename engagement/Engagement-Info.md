# Engagement Info

> Complete this document before reconnaissance. Do not store passwords, session tokens, API keys, private certificates, or raw personal data here.

## Identification

| Field | Value |
|---|---|
| Client | `EDIT_ME` |
| Project name | `EDIT_ME` |
| Engagement ID | `EDIT_ME` |
| Assessment type | `Web application penetration test` |
| Owner/pentest firm | `EDIT_ME` |
| Primary tester | `EDIT_ME` |
| Date/time zone | `EDIT_ME` |
| Authorization reference | `EDIT_ME` |

## Scope

| Field | Value |
|---|---|
| Primary URL | `https://EDIT_ME/` |
| Approved hostnames | `EDIT_ME` |
| Approved IPs/CIDRs | `EDIT_ME` |
| Approved ports/protocols | `EDIT_ME` |
| Excluded assets | `EDIT_ME` |
| Start (UTC) | `EDIT_ME` |
| End (UTC) | `EDIT_ME` |
| Emergency contact | `EDIT_ME` |
| Stop condition/contact | `EDIT_ME` |

## Tooling and routing

| Field | Value |
|---|---|
| Burp MCP endpoint | `http://127.0.0.1:9876` |
| Browser | `EDIT_ME` |
| Burp project/evidence location | `private/` or approved secure location; never commit it |
| Direct target traffic permitted? | `NO — use Burp MCP unless explicitly changed` |
| OOB listener | `NOT_APPROVED_UNTIL_FILLED` |

## Supplied roles

The canonical role order is:

1. Super Admin / highest privilege
2. Admin
3. Supervisor
4. Agent / lowest privilege

Role labels, usernames, tenant assignment, and secret references belong in `engagement/Roles-and-Credentials.md`. Passwords belong in a password manager or ignored `private/credentials.env` file. Run `scripts/build-machine-state.py` to generate `config/roles.csv`.

## Authorization boundaries

- [ ] Read-only reconnaissance approved
- [ ] Authenticated testing approved
- [ ] Low-impact input canaries approved
- [ ] Disposable object creation and cleanup approved
- [ ] File-upload tests approved
- [ ] SSRF/OOB tests approved
- [ ] Request-smuggling/persistent-connection tests approved
- [ ] WebSocket frame/message tests approved
- [ ] Password/recovery/lockout tests approved
- [ ] Email/webhook/report delivery tests approved
- [ ] Third-party/CCP/WebRTC actions approved
- [ ] Concurrency tests approved
- [ ] Destructive or irreversible actions approved separately

## Engagement-specific notes

- Default tenant(s): `EDIT_ME`
- Test data/fixture namespace: `EDIT_ME`
- Allowed disposable destination(s): `EDIT_ME`
- Required cleanup procedure: `EDIT_ME`
- Known maintenance windows: `EDIT_ME`
- Reporting requirements: `EDIT_ME`
