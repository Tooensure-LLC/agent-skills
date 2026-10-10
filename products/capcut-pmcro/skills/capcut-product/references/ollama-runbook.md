# Ollama runbook

The local model may be slow or unable to call tools. Keep the skill executable
as a deterministic text protocol.

## Response budget

Plan for a 16,384-token context:

- role prompt: at most 2,000 tokens;
- loaded skill text: at most 4,000 tokens;
- user input and conversation: at most 8,000 tokens;
- reserved response: at least 2,000 tokens.

## Required response shape

Return these headings in order:

1. `PMCR-O FRAME`
2. `I AM`
3. `TARGET`
4. `USER ACTIONS`
5. `AGENT ACTIONS`
6. `EVIDENCE REQUIRED`
7. `STATUS`
8. `NEXT SEED`

Use one action per numbered line. Do not invent a browser, desktop session,
installation, login, export, file, or checker result. If a target is missing,
use `export-guide`. If a tool is unavailable, say `manual action required`.

Never emit private chain-of-thought. Emit concise decisions, observable
actions, evidence references, uncertainty, and the next bounded seed.
