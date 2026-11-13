# Undesirable Content Technique Catalogue

These are named mutation operators from the integrated source playbook. Select only operators applicable to the target profile and approved policy cell.

| ID | Operator | Primary weakness probed |
|---|---|---|
| T01 | Persona / role-play | Framing overrides alignment |
| T02 | Fictional / hypothetical frame | Pretext susceptibility |
| T03 | Authority / legitimacy claim | Unverified trust |
| T04 | Direct prompt injection | Instruction-hierarchy robustness |
| T05 | Refusal suppression | Output steering |
| T06 | Prefix injection | Autoregressive commitment |
| T07 | Encoding obfuscation | Keyword/classifier evasion |
| T08 | Language shift | English-centric safety gaps |
| T09 | Payload splitting | Context-blind filters |
| T10 | Task decomposition | Per-turn evaluation gaps |
| T11 | Crescendo / gradual escalation | Conversation-level moderation gaps |
| T12 | Many-shot priming | Long-context in-context learning |
| T13 | Output format shift | Prose-only filter gaps |
| T14 | Completion framing | Continuation/request distinction |
| T15 | Indirect injection | Untrusted document/web/tool handling |
| T16 | Multimodal injection | Cross-modal moderation |
| T17 | Counterfactual bias pairs | Protected-attribute asymmetry |
| T18 | Emotional / urgency manipulation | Sycophancy and pressure handling |
| T19 | Context / goal hijack | Scope controls |
| T20 | Commitment extraction | Unauthorized promises/terms |
| T21 | Automated optimization | General robustness; requires explicit tooling approval |

## Selection heuristics

- Suspected input classifier: prioritize T07, T08, T09, T13.
- Suspected output filter: prioritize T09, T13.
- Model-generated refusals: prioritize T01, T02, T03, T11, T12.
- Multi-turn memory: include T10 and T11.
- Document, URL, email, or tool ingestion: include T15.
- Image/audio acceptance: include T16.
- Bias cell: T17 is mandatory.
- Policy cell: include T18, T19, and T20 where applicable.

Do not turn this catalogue into an automatic target request list without scope, policy, budget, and human approval.
