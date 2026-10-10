param([string]$Root = (Split-Path -Parent $PSScriptRoot))
$ErrorActionPreference = "Stop"
$rootPath = (Resolve-Path -LiteralPath $Root).Path
foreach ($relative in @("SKILL.md", "agents\openai.yaml", "agents\capcut-product.json", "references\sample-prompts.md", "references\product-contract.md", "references\platform-self-update.md", "references\capcut-export-guide.md", "references\ollama-runbook.md", "references\init.md", "references\pmcro-task.md", "scripts\init.py", "assets\README.md", "tests\README.md")) {
  if (-not (Test-Path -LiteralPath (Join-Path $rootPath $relative) -PathType Leaf)) { throw "missing $relative" }
}
Write-Output "PASS: capcut-agent skill surface"
