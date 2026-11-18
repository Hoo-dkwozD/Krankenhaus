# Resource Locator

> Human-readable source. This is an index, not a payload dump. Add local files or online locators with provenance and review status.

| Resource ID | Vulnerability family | Resource type | Locator | Authority/provenance | Version/date | Enabled | Engagement use | Notes |
|---|---|---|---|---|---|---|---|---|
| RB-0001 | APP-INJ-01 | local or online | `EDIT_ME` | `EDIT_ME` | `EDIT_ME` | false | `EDIT_ME` | Example only; replace or disable |
| RB-0002 | APP-INJ-01 | online payload reference | `https://github.com/payload-box/xss-payload-list/tree/main` | Payload Box GitHub repository | Rolling repository; verify at campaign start | true | XSS payload discovery and context-specific variant selection | Review current content, licensing, and applicability; never send the full list automatically |
| RB-0003 | APP-INJ-01 | online cheat sheet | `https://portswigger.net/web-security/cross-site-scripting/cheat-sheet` | PortSwigger Web Security Academy / PortSwigger Research | Actively maintained; verify page date at campaign start | true | XSS context, event, tag, browser, framework, encoding, and filter-bypass research | Use for context-specific selection and verification; do not send the full vector set automatically |
| RB-0004 | APP-INJ-02 | online payload reference | `https://github.com/payload-box/sql-injection-payload-list` | Payload Box GitHub repository | Rolling repository; verify at campaign start | true | SQLi payload discovery and DBMS-specific variant selection | Review current content, licensing, and applicability; never send the full list automatically |
| RB-0005 | APP-INJ-02 | online cheat sheet | `https://portswigger.net/web-security/sql-injection/cheat-sheet` | PortSwigger Web Security Academy | Actively maintained; verify page date at campaign start | true | SQLi syntax, DBMS-specific behavior, blind/error/time-based research, and verification | Use only for approved low-impact checks; external-side-effect or OOB techniques require separate authorization |

## Resource handling rules

- Prefer primary/authoritative sources and stable versioned URLs.
- Record licenses or usage restrictions for copied material.
- Keep local banks under ignored/private storage when they contain sensitive or licensed content.
- Do not automatically send every resource payload to a target; map resources to an approved finding, input point, role, and batch first.
- Record the resource version used for each campaign so results are reproducible.
