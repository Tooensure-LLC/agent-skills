---
name: capcut-product
description: Generate and check a bounded CapCut-oriented content-product scaffold through PMCR-O without claiming official CapCut access or adding upload authority.
---

# CapCut product scaffold

Use this skill to shape a CapCut-oriented product repository from declared
intent, identity, and local resources. It produces a provider-neutral contract
and trail. It does not log into CapCut, store credentials, upload media, or
publish content.

## Required flow

Run the public phases in order:

`ORCHESTRATE -> PLAN -> MAKE -> CHECK -> REFLECT`

The orchestrator binds the grant and target path. The planner selects the
smallest artifact graph. The maker writes only the declared scaffold. A fresh
checker reruns the validators and issues the only verdict. The reflector waits
for that verdict, records an earned constraint, and emits one unexecuted seed.

## Input

Accept a product request containing owner, identity, target repository/path,
parent marketplace ref, content intent, acceptance criteria, and non-goals.
Require a validated `product.manifest.json`, `marketplace.source.json`, and
`autonomy-grant.example.json` before writing.

## Output

Return the product manifest, required agent surfaces, generic trail, validator
evidence, provenance, checker verdict, and one unexecuted next seed. Mark
simulation separately from execution evidence. A scaffold is not proof of a
CapCut integration.

## Boundaries

- Never request or copy credentials, recovery codes, or private provider data.
- Never add upload, publishing, account, or monetization authority implicitly.
- Never let the maker approve its own output.
- Never execute the reflector seed automatically.
- Stop on missing parent provenance, scope changes, or an unavailable checker.
