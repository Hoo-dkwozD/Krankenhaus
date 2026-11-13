# LLM Evidence

Store full prompt/response transcripts, model metadata, judge input, and classifier output only in approved encrypted/access-controlled storage, normally under ignored `private/` storage or an approved evidence system.

Tracked evidence should contain sanitized metadata and redacted excerpts only:

- Target ID and exact allowlisted endpoint.
- Prompt/response field paths.
- Model/version/parameters.
- Session/conversation reference.
- Policy cell and technique.
- Status, score, confidence, and reproducibility.
- Human-review and escalation result.

Never put full harmful output, credentials, real personal data, or unrestricted transcripts in normal Markdown, reports, or agent messages.
