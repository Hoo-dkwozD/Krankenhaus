# LLM Engagement Info

> Human-readable source. Complete before any LLM target request. Do not store API keys, passwords, raw harmful transcripts, or unnecessary personal data here.

## Identification and authorization

| Field | Value |
|---|---|
| Mode | `LLM testing` |
| Client | `EDIT_ME` |
| Project name | `EDIT_ME` |
| Engagement ID | `EDIT_ME` |
| Authorized by | `EDIT_ME` |
| Authorization reference | `EDIT_ME` |
| Environment | `staging | production | EDIT_ME` |
| Start (UTC) | `EDIT_ME` |
| End (UTC) | `EDIT_ME` |
| Jurisdictions | `EDIT_ME` |
| Languages supported | `EDIT_ME` |
| Languages to probe | `EDIT_ME` |

## Business and user context

| Field | Value |
|---|---|
| Use-case description | `EDIT_ME` |
| Explicitly in-scope uses | `EDIT_ME` |
| Explicitly out-of-scope uses | `EDIT_ME` |
| Primary audience | `EDIT_ME` |
| Age range / minors possible | `EDIT_ME` |
| Vulnerable populations | `EDIT_ME` |
| User roles/personas | `EDIT_ME` |
| Key workflows | `EDIT_ME` |
| Regulated or high-impact decisions | `EDIT_ME` |
| Required escalation behavior | `EDIT_ME` |
| Required disclaimers | `EDIT_ME` |
| Allowed tone/persona | `EDIT_ME` |
| Prohibited commitments/actions | `EDIT_ME` |
| Client policy references | `EDIT_ME` |
| Legal or compliance guidance | `EDIT_ME` |
| Reportable success threshold | `EDIT_ME` |
| Benign control examples | `EDIT_ME` |

## Approvals and safety gates

- [ ] Written authorization names the LLM target, endpoints, environment, and dates.
- [ ] Human lead approved the policy matrix and context.
- [ ] Legal/compliance review completed for hazardous or jurisdiction-specific categories.
- [ ] Target environment confirmed; production testing has explicit approval if applicable.
- [ ] Attacker and judge model providers permit this evaluation, or models are self-hosted/approved.
- [ ] Evidence storage is access-controlled and retention is agreed.
- [ ] Kill switch is tested.
- [ ] Human reviewer and escalation contact are assigned.
- [ ] Tester welfare/exposure controls are defined.
- [ ] Hard exclusions and proxy-only categories are recorded in the policy matrix.

## Budget and evidence

| Field | Value |
|---|---|
| Max cost (USD) | `EDIT_ME` |
| Max requests per minute | `EDIT_ME` |
| Max turns per conversation | `EDIT_ME` |
| Max attempts per objective | `EDIT_ME` |
| Reproduction trials (N) | `EDIT_ME` |
| Confirm threshold | `EDIT_ME` |
| Evidence store reference | `private/` or approved encrypted store |
| Retention days | `EDIT_ME` |
| Report redaction required | `true` |
| Escalation contact | `EDIT_ME` |

## Agent roles

| Agent role | Model/provider | Credential reference | Different family from target? | Approved | Notes |
|---|---|---|---|---|---|
| Orchestrator | `EDIT_ME` | `private/credentials.env` or vault | n/a | false | Scope, budget, stop rules |
| Attacker A | `EDIT_ME` | `private/credentials.env` or vault | `EDIT_ME` | false | Must be permitted for red-team use |
| Attacker B | `EDIT_ME` | `private/credentials.env` or vault | `EDIT_ME` | false | Diversity model |
| Judge A | `EDIT_ME` | `private/credentials.env` or vault | `EDIT_ME` | false | Prefer different family from target |
| Judge B | `EDIT_ME` | `private/credentials.env` or vault | `EDIT_ME` | false | Optional agreement check |
| Classifier(s) | `EDIT_ME` | `private/credentials.env` or vault | n/a | false | Record provider and version |
