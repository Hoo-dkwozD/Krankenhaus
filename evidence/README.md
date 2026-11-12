# Evidence

Store sanitized, reproducible evidence here. Keep raw Burp projects, raw HTTP archives, full responses, tokens, credentials, and unnecessary PII under ignored `private/` storage.

Recommended names:

```text
YYYY-MM-DD_<finding-or-phase>_<role>_<batch>_<short-description>.md
```

Each record should state:

- UTC timestamp
- Role and tenant
- Method, host, path, and relevant query/body fields
- Sanitized headers and response status/schema
- Preconditions, expected behavior, observed behavior
- Control result and cleanup result
- Burp MCP evidence reference

Do not call an endpoint `negative` unless the exact role, variant, object, tenant, and protocol boundary was tested.
