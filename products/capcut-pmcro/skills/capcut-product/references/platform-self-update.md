# Platform-gated self-update

`capcut-agent` can improve its declarative skill package when the active host
declares a compatible skill-creator capability. This is a governed proposal,
not unrestricted self-modification.

## Route

1. Read `platform-capabilities.example.json` and the active platform envelope.
2. If `skill-creator` is unavailable, emit a manual next seed and stop.
3. If available, invoke the platform's skill creator with the existing grant.
4. Permit only skill material: `skills/`, `references/`, `scripts/`, `assets/`,
   and `tests/`.
5. Record the generated diff and tool result in the trail.
6. Send the proposal to a separate checker; the maker cannot approve it.
7. Reflect one earned constraint and one unexecuted next seed.

The self-update route cannot rewrite the autonomy grant, checker authority,
orchestrator charter, or prior trail history. It cannot add credentials,
account automation, upload, or external publishing authority. A future
`capcut-agent-computer-use` capability therefore remains simulation-only until
its own platform contract and checker evidence exist.
