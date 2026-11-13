# LLM Testing Plan

> Human-readable source. Dynamic vulnerability discovery is intentionally blank for this phase. The active list contains one placeholder objective from the integrated undesirable-content playbook.

## Dynamic objective gathering

- Discovery method: `EDIT_ME`
- Discovery sources: `EDIT_ME`
- Last discovery date: `EDIT_ME`
- Human approval required before activation: `true`
- Dynamic list status: `Not implemented — placeholder list used`

## Active objectives

| Objective ID | Title | Playbook reference | Target IDs | Policy cells | Baseline required | Adversarial required | Reproduction N | Status | Notes |
|---|---|---|---|---|---|---|---:|---|---|
| LLM-UC-01 | Undesirable Content | `llm/playbooks/undesirable-content/Playbook-Integration.md` | TARGET-001 | LLM-UC-01 | true | true | EDIT_ME | Planned | Context and endpoint must be completed first |

## Campaign sequencing

1. Complete the LLM engagement context and policy matrix.
2. Specify the exact prompt-insertion endpoint, method, field/path, response path, auth reference, and production-like parameters.
3. Record target reconnaissance: model/guardrails, output filters, context/memory, languages, rendering, RAG, and tools.
4. Run direct baseline prompts and benign controls before adversarial techniques.
5. Select approved techniques from the integrated playbook based on the target profile.
6. Enforce code-level host, endpoint, budget, rate, turn, and stop rules.
7. Reproduce candidate outcomes N times with fixed prompts and fresh sessions where applicable.
8. Use paraphrase variants, judge calibration, and mandatory human review.
9. Report redacted excerpts and keep full transcripts in approved evidence storage.
