# Evidence

Store sanitized, reproducible evidence here. Keep raw Burp projects, raw HTTP archives, full responses, tokens, credentials, and unnecessary PII under ignored `private/` storage.

Use filenames that identify the finding or phase, role/context, batch, endpoint, and date when those details are useful. The naming format is a guide, not a required schema.

Each evidence record should include whatever is needed to reproduce the result, such as:

- Timestamp or run reference.
- Role, account, tenant, object, or workflow context when applicable.
- Method, host, path, protocol, and relevant query/body fields.
- Sanitized headers, status, response schema, and meaningful state changes.
- Preconditions, expected behavior, observed behavior, control comparisons, and cleanup.
- UI/API or WebSocket comparison details where relevant.
- Burp MCP or other evidence reference.

Do not call a boundary negative unless the exact tested role/context, variant, object, input, and protocol boundary are recorded.
