# [ID] — [Title]

Use this record for a candidate or confirmed finding. Keep it concise when the issue is simple and expand the free-form sections when the application or impact requires more detail.

## Status and evidence

- Status: `Observed — needs confirmation`
- Date/time or run reference:
- Evidence files/Burp references:
- Finding or batch references:

## Boundary

- Target URL/host:
- Role or account context:
- Tenant/organization/object context, if applicable:
- Endpoint, method, protocol, and UI/API workflow:
- Input, field, message, sink, or state transition:
- Resource/technique reference:

## Preconditions and expected control

Describe the precondition, the expected authorization/validation/safety behavior, and any relevant control role, object, tenant, input, or UI path.

## Reproduction

1.
2.
3.

Use sanitized requests and responses. Never include passwords, tokens, API keys, or unnecessary PII.

## Observed result and coverage

Describe the observed behavior, affected roles/objects/instances, UI/API difference if relevant, and all tested variants. Record remaining untested boundaries instead of implying complete coverage.

## Postcondition, replay, and cleanup

Describe any affected state, original request replay, control comparison, cleanup action, cleanup verification, or `Not applicable`.

## Impact and remediation

Describe confidentiality, integrity, availability, business impact, likelihood, affected scope, remediation, and retest criteria. Add any context-specific detail needed by the engagement.

## Residual boundaries

Record browser, API, WebSocket, mutation, cross-tenant, file, external-side-effect, parser, role, or other boundaries that were not tested or could not be reproduced.
