# Tooensure CapCut PMCR-O product scaffold

This is a bounded, provider-neutral scaffold for a CapCut-oriented content
product. It is a derived child of the checked PMCR-O marketplace branch:

```text
parent: pmcr-o/skills
ref: feature/thought-transfer-pmcro-23526a8
commit: 84f70f8e1b281ee741934ec54de3173bbc972f8b
target: Tooensure-LLC/agent-skills/products/capcut-pmcro
```

The scaffold demonstrates the product contract, skill surface, agent roles,
generic PMCR-O trail, and finite autonomy grant. It does not claim official
CapCut API access, upload capability, account authority, monetization, or a
market outcome. Any real integration must be introduced as a separately
validated adapter with its own checker cycle.

## PMCR-O sequence

```text
ORCHESTRATE -> PLAN -> MAKE -> CHECK -> REFLECT
```

The independent checker is a separate role surface and may issue the only
`PASS`, `LOOP`, or `HALT` verdict. The reflector records an earned constraint
and one unexecuted next seed; it never executes that seed.

## Local validation

```text
pwsh -NoProfile -ExecutionPolicy Bypass -File scripts/validate.ps1
python scripts/validate_trail.py --trail .pmcro/trails/example.jsonl
```

`autoApprove` means “continue inside this existing grant.” It never authorizes
credentials, deletion, external publishing, scope changes, or CapCut account
actions. Those require a new grant and checker cycle.

## Product surfaces

- `skills/capcut-product/` — installable skill with required agent metadata,
  references, scripts, assets, tests, and prompts.
- `.agents/agents/` — orchestrator, independent checker, and reflector roles.
- `.pmcro/` — generic trail contract and replayable example trail.
- `marketplace.source.json` — provenance and parent-child mapping.
- `product.request.json` — the bounded product intent and acceptance contract.
