# PMCR-O task envelope

Use a PMCR-O task when a user wants to give the skill more than `init`.

Minimum fields:

```json
{
  "apiVersion": "pmcro.task/v1",
  "command": "init",
  "intent": "...",
  "target": "export-guide",
  "mode": "simulate",
  "authority": "user-directed"
}
```

The task is a request, not a grant. The orchestrator validates the target,
resources, platform capability, and autonomy level before routing work.

Return the task as a small packet with `I AM`, `TARGET`, `USER ACTIONS`,
`AGENT ACTIONS`, `EVIDENCE REQUIRED`, `STATUS`, and `NEXT SEED`. Keep the next
seed unexecuted.
