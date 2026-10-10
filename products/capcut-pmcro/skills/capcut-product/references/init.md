# `init` entrypoint

The marketplace is usable from a one-word start:

```text
init
```

The agent must default to `export-guide`, create an activation packet, and ask
which target the user wants. It must not install CapCut, authenticate, open a
browser, control a desktop, or claim execution during initialization.

Equivalent local command:

```text
python scripts/init.py
```

Machine-readable packet:

```text
python scripts/init.py --json
```

Explicit target:

```text
python scripts/init.py --target browser-session
python scripts/init.py --target desktop-session
```

The target is still subject to the platform capability contract and a separate
checker. A target request is not permission to use it.
