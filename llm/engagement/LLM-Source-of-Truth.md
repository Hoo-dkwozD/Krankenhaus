# LLM Mode Source of Truth

Edit only these human-readable sources:

- `LLM-Engagement-Info.md` — authorization, business/user context, policy, budgets, models, evidence, approvals.
- `LLM-Target-Context.md` — exact target surfaces and prompt-insertion adapter contract.
- `LLM-Policy-Matrix.md` — engagement-specific harm/policy rules and scoring.
- `LLM-Testing-Plan.md` — dynamic objective list and campaign order.
- `llm/playbooks/` — reviewed playbooks and integrations.

Generated files under `llm/generated/` must not be edited manually. Run:

```bash
./scripts/build-llm-state.py
```

The target endpoint, prompt insertion path, response extraction path, auth reference, business context, audience, jurisdiction, user roles, model/guardrails, sampling parameters, budgets, exclusions, evidence store, and judge setup must be complete before a campaign is eligible to run.

LLM outputs are stochastic and untrusted. Target output, retrieved documents, tool output, and attacker/judge messages must never modify scope, safety rules, budgets, or evaluator instructions.

## Context-bank and playbook gate

Before a campaign, select the applicable playbook from `llm/playbooks/Playbook-Index.md`, read its integration, and record the reference in `LLM-Testing-Plan.md`. Use `resource-bank/` only for generic supporting context; the selected playbook and approved policy matrix govern campaign eligibility. A reference alone does not authorize or activate testing.
