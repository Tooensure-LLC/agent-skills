---
name: capcut-agent
description: Generate and check a bounded CapCut Agent scaffold through PMCR-O without claiming official CapCut access or adding upload authority.
---

# CapCut Agent scaffold

Use this skill to shape a CapCut Agent product repository from declared
intent, identity, and local resources. It produces a provider-neutral contract
and trail. It does not log into CapCut, store credentials, upload media, or
publish content.

The default execution mode is `export-guide`. The skill does not install
CapCut. It emits a deterministic packet that a slow local model can follow.
Choose `browser-session` or `desktop-session` only when the platform envelope
declares the required browser or computer-use capability.

## Start with `init`

When the user says only `init`, run `scripts/init.py` or construct its same
packet. Default to `export-guide`, show the user the three target choices, and
wait for target confirmation. A target request is not permission to use a
browser or desktop surface.

When the user supplies a PMCR-O task, validate its `apiVersion`, target,
authority, resources, and acceptance criteria before routing it.

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

Also require an execution target: `export-guide`, `browser-session`, or
`desktop-session`. If it is missing, use `export-guide`.

Before a self-update, read `platform-capabilities.example.json`. Invoke the
platform skill creator only when the active platform declares that capability;
otherwise emit a manual next seed. Keep self-update limited to declarative
skill material and route the proposal through a separate checker.

## Output

Return the product manifest, required agent surfaces, generic trail, validator
evidence, provenance, checker verdict, and one unexecuted next seed. The
default output is `execution-packet.example.json` shaped as:

`I AM -> TARGET -> USER ACTIONS -> AGENT ACTIONS -> EVIDENCE -> STATUS -> NEXT SEED`

Mark simulation separately from execution evidence. A guide is not proof that
CapCut ran, rendered, or exported anything.

## Target rules

- `export-guide`: give numbered instructions; require the user to perform
  installation, sign-in, editing, and export.
- `browser-session`: require an approved browser surface and user-authorized
  session; do not install software or request credentials in the skill.
- `desktop-session`: require CapCut Desktop already installed on the user's
  computer and an approved computer-use surface; do not install or authenticate.
- Unknown target: fall back to `export-guide` and emit a manual next seed.

Use `references/init.md` for activation, `references/pmcro-task.md` for task
envelopes, `references/capcut-export-guide.md` for platform-specific export
steps, and `references/ollama-runbook.md` for small-model response discipline.

## Boundaries

- Never request or copy credentials, recovery codes, or private provider data.
- Never add upload, publishing, account, or monetization authority implicitly.
- Never let the maker approve its own output.
- Never execute the reflector seed automatically.
- Never claim an export from an instruction packet.
- Never confuse the user's computer with the agent's browser or computer.
- Stop on missing parent provenance, scope changes, or an unavailable checker.

The public identity is `capcut-agent`; the governed package is `capcut-pmcro`.
Child capability names must use the `capcut-agent-*` namespace and must carry
their own status, mode, authority, and checker evidence. `capcut-agent-computer-use`
is not executable in this scaffold.
