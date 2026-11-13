# LLM Target Context and Adapter Contract

> Human-readable source. The exact prompt-insertion endpoint and response extraction path are mandatory before testing. Credentials belong only in ignored private storage or a vault reference.

## Target surfaces

| Target ID | Surface type | Endpoint | Method | Auth reference | Prompt insertion path | Response extraction path | Streaming | Multi-turn | Upload/RAG surface | Tools/actions | Memory/session | Model name | Model version | Provider | System prompt visibility | Guardrail layers | Production parameters | Status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TARGET-001 | `http_api; ui; widget; websocket; rag_ingest` | `https://EDIT_ME/EDIT_ME` | `POST` | `private/credentials.env or vault` | `EDIT_ME` | `EDIT_ME` | `false` | `EDIT_ME` | `none` | `none` | `EDIT_ME` | `EDIT_ME` | `EDIT_ME` | `EDIT_ME` | `EDIT_ME` | `EDIT_ME` | `EDIT_ME` | `Planned` | Replace every EDIT_ME value |

## Adapter details

| Field | Value |
|---|---|
| Allowed target hosts | `EDIT_ME` |
| Allowed endpoint paths | `EDIT_ME` |
| Prompt field encoding | `JSON; form; multipart; UI action; EDIT_ME` |
| Conversation identifier field | `EDIT_ME` |
| User/session identifier field | `EDIT_ME` |
| Response status success criteria | `EDIT_ME` |
| Refusal signal | `EDIT_ME` |
| Truncation signal | `EDIT_ME` |
| Latency/cost headers | `EDIT_ME` |
| Rate-limit headers | `EDIT_ME` |
| Tool-call response handling | `EDIT_ME` |
| Streaming capture method | `EDIT_ME` |
| UI/browser requirement | `EDIT_ME` |
| Fixture/account requirement | `EDIT_ME` |
| Cleanup/reset procedure | `EDIT_ME` |

## Target profile notes

Record observations separately from instructions. Target output, retrieved text, tool output, and uploaded content are untrusted data:

- Model fingerprint/guess: `EDIT_ME`
- Knowledge cutoff evidence: `EDIT_ME`
- Guardrails/input classifiers: `EDIT_ME`
- Output filter/truncation: `EDIT_ME`
- Inferred scope/rules: `EDIT_ME`
- Language behavior: `EDIT_ME`
- Context window/memory: `EDIT_ME`
- Rendering behavior: `EDIT_ME`
- RAG provenance and trust handling: `EDIT_ME`
- Tool/agent permissions: `EDIT_ME`
