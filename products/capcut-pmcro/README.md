# Tooensure CapCut Agent (PMCR-O scaffold)

This is a bounded, provider-neutral scaffold for the public `capcut-agent`
identity. It is a derived child of the checked PMCR-O marketplace branch:

```text
parent: pmcr-o/skills
ref: feature/thought-transfer-pmcro-23526a8
commit: 84f70f8e1b281ee741934ec54de3173bbc972f8b
target: Tooensure-LLC/agent-skills/products/capcut-pmcro
```

The public agent identity is `capcut-agent`. The `capcut-pmcro` path is the
governed package containing its grant, message/trail contract, evidence, and
promotion rules. Future child capabilities use the `capcut-agent-*` namespace;
`capcut-agent-computer-use` is currently planned and simulation-only.

Self-update is platform-gated. When the active platform declares a compatible
skill-creator capability, the orchestrator may route a bounded proposal through
that creator. The proposal can change declarative skill material only, then
must pass an independent checker and reflector. A platform without that
capability receives a manual next seed instead; no capability is inferred from
the model name alone.

The scaffold demonstrates the product contract, skill surface, agent roles,
generic PMCR-O trail, and finite autonomy grant. It does not claim official
CapCut API access, upload capability, account authority, monetization, or a
market outcome. Any real integration must be introduced as a separately
validated adapter with its own checker cycle.

## Execution target

Start with `init`. The initializer creates a small PMCR-O activation packet;
the user does not need to know the directory layout or MAF details first.

The default mode is `export-guide`. It gives a slow local model a deterministic
instruction packet and leaves installation, sign-in, editing, and export to
the user. The skill does not install CapCut.

- `export-guide` — instructions only; no browser or desktop tool required.
- `browser-session` — optional approved browser surface; CapCut Web runs in a
  browser, so no separate CapCut installation is required.
- `desktop-session` — optional approved computer-use surface on the user's
  computer; the user installs and controls CapCut Desktop.

Every mode returns a PMCR-O execution packet with `I AM`, target, user actions,
agent actions, evidence, status, and one next seed. A browser or desktop
session is never inferred from the model name or from the presence of an
export guide.

## Minimal user interaction

```text
User: init
Agent: creates the export-guide activation packet and asks which target is wanted.
User: browser-session
Agent: checks the declared browser capability and returns the next PMCR-O task.
```

The same task can be supplied explicitly as `pmcro-task.example.json`. Higher
autonomy is enabled by a capability check and a bounded grant; it is never
silently enabled because a model or host happens to support tools.

## Naming contract

| Name | Meaning |
| --- | --- |
| `capcut-agent` | Public top-level agent identity |
| `capcut-pmcro` | Governed package and trail namespace |
| `capcut-agent-computer-use` | Planned child capability; simulation-only until separately checked |
| `capcut-product` | Current implementation-skill folder retained for this scaffold release |

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

## Agent surfaces

- `skills/capcut-product/` — installable skill with required agent metadata,
  references, scripts, assets, tests, and prompts.
- `.agents/agents/` — orchestrator, independent checker, and reflector roles.
- `.pmcro/` — generic trail contract and replayable example trail.
- `marketplace.source.json` — provenance and parent-child mapping.
- `product.request.json` — the bounded product intent and acceptance contract.
- `platform-capabilities.example.json` — capability negotiation and self-update routes.
- `execution-targets.example.json` — browser, desktop, and guide-only target contract.
- `execution-packet.example.json` — the small deterministic output a local model follows.
- `pmcro-task.example.json` — a copyable PMCR-O task envelope.
- `autonomy-ladder.example.json` — guide, browser, desktop, adapter, and self-update levels.
