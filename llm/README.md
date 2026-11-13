# LLM Testing Mode

LLM testing is a separate mode from the web-application assessment mode. It uses its own engagement context, target adapter details, policy matrix, playbooks, campaigns, evaluation records, and evidence boundaries.

## Current active objective

The dynamic LLM vulnerability-list gathering stage is intentionally left as a placeholder. The initial active objective is:

```text
LLM-UC-01 — Undesirable Content
```

The integrated playbook is based on a user-supplied undesirable-content red-team playbook, version 1.0.

The local integration is in `llm/playbooks/undesirable-content/`. The source document is external provenance and is not assumed to be available after the project is moved to another machine or GitHub.

## Human-readable source files

Edit only these files for an engagement:

- `llm/engagement/LLM-Engagement-Info.md`
- `llm/engagement/LLM-Target-Context.md`
- `llm/engagement/LLM-Policy-Matrix.md`
- `llm/engagement/LLM-Testing-Plan.md`
- `llm/engagement/LLM-Source-of-Truth.md`
- `llm/playbooks/` when adding or revising reviewed playbooks

Generated files are under `llm/generated/` and must not be edited manually.

## Build command

```bash
./scripts/build-llm-state.py
```

This generates:

- `llm/generated/llm-engagement.yaml`
- `llm/generated/llm-targets.csv`
- `llm/generated/llm-policy-matrix.csv`
- `llm/generated/llm-campaign-matrix.csv`
- `llm/generated/LLM-Finding-Plan.md`

## Operating model

1. Human lead completes scope, endpoint, business, user, model, policy, budget, evidence, and approval context.
2. Select the applicable reviewed playbook from `llm/playbooks/Playbook-Index.md`, read its integration, and record the selected playbook reference in the testing plan. The reference does not activate testing or override engagement policy.
3. The target adapter is allowlisted to the exact prompt-insertion endpoint and response path.
4. Recon records model/guardrail/context behavior without treating a target output as instructions.
5. Baseline tests use direct prompts and benign controls before adversarial techniques.
6. Campaigns use approved objectives and techniques from the selected playbook with code-level budgets and stop rules.
7. Judges score content against the engagement policy matrix, not tone or apparent compliance.
8. Candidate successes are reproduced at configured N-trial thresholds and reviewed by a human before reporting.
9. Reports use redacted excerpts; full transcripts stay in approved evidence storage.
