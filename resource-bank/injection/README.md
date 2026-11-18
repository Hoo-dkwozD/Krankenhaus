# Injection Resources

Reserved for XSS, SQL/NoSQL injection, SSTI, command injection, traversal, uploads, SSRF, XML, deserialization, pollution, CRLF, request smuggling, and protocol-specific references. Payload resources require separate review and scope mapping.

For XSS and SQL injection, the LLM must retrieve the enabled resources in `resource-bank/Resource-Locator.md` before testing and record the current relevant sections in `plans/Resource-Review.md`. The review should identify context, parser, framework, browser, DBMS, encoding, case, whitespace, comment, content-type, error, boolean, time, file, SVG, multipart, and filter variants that apply to the discovered surface. Do not rely on remembered payloads or send an entire external list automatically.