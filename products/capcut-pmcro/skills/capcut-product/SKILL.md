---
name: capcut-agent
description: Generate and check a bounded CapCut Agent scaffold through PMCR-O without claiming official CapCut access or adding upload authority.
---

# CapCut Agent scaffold

Use this skill to shape a CapCut Agent product repository from declared
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

Accept an agent product request containing owner, identity, target repository/path,
parent marketplace ref, content intent, acceptance criteria, and non-goals.
Require a validated `product.manifest.json`, `marketplace.source.json`, and
`autonomy-grant.example.json` before writing.

Before a self-update, read `platform-capabilities.example.json`. Invoke the
platform skill creator only when the active platform declares that capability;
otherwise emit a manual next seed. Keep self-update limited to declarative
skill material and route the proposal through a separate checker.

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

The public identity is `capcut-agent`; the governed package is `capcut-pmcro`.
Child capability names must use the `capcut-agent-*` namespace and must carry
their own status, mode, authority, and checker evidence. `capcut-agent-computer-use`
is not executable in this scaffold.
