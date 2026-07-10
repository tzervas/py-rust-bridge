
# AGENTS.md — py-rust-bridge

**Use Tero + cabal-devmelopner for work here.**

## Tero (Layer-1 corpus index)

Repo has `docs/tero-index/index.json` (generated/ refreshed via tero-mcp/scripts/generate_lite_index.py).

**Rule:** Use tero queries before large greps or assumptions.
- Grok: tero__text_search / query_by_id (token "local-dev")
- Direct: tero-mcp-lite --index docs/tero-index/index.json
- cabal-devmelopner: auto-detects local index when run from within this tree (or set TERO_INDEX_PATH).

Example:
```bash
cd /root/git/py-rust-bridge
# agent with context:
uv run --project ../cabal-devmelopner cabal-devmelopner "task description here" --use-tero
```

Citations point at file:line — open them.

## Working with cabal-devmelopner agent tool

This project is prepared for integration:
- Tero index committed on chore/tero-index-cabal-ready (and PRable to dev)
- Local auto index support in cabal
- This AGENTS.md

**PR flow (protect main/dev):**
- Create/checkout feature or chore branch
- Make changes (agent will often use working branch)
- PR the branch → `dev` (then dev → main when ready)

## Local checks

Look for:
- scripts/check.sh
- Cargo.toml / pyproject.toml + standard commands (cargo test, uv run pytest, ruff, etc.)

Run checks before considering work complete.

## Further reading

- README.md
- docs/ROADMAP.md or ROADMAP.md (if present)
- docs/ASSESSMENT.md or similar for intent/gaps
- ../cabal-devmelopner/docs/* for agent architecture
- ../tero-mcp for how indexes are built and served

Leave mycelium isolated; all coordination here targets the other repos + cabal.

## Hygiene + Tero landing (chore/tero-index-cabal-ready, 2026-07-09 appended)

Tero-first (via /root/git/scripts/tero.sh identify + text_search "chore tero hygiene check ROADMAP scaffolding" + cites to AGENTS local-checks, tero-index, readme). 

- Added ruff to dev-deps + [tool.ruff] config in pyproject.toml (parity with cabal).
- Added scripts/check.sh (modeled on search-box/cabal + tero-mcp): uv sync if present → ruff format/check (fix mode), mypy advisory, pytest -q; fallback pytest; + tero-mcp/scripts/generate_lite_index.py --root .
- Added minimal docs/ROADMAP.md (scaffolding role, tero/hygiene ready, links workspace plan.md § hygiene-thin-repos + wsfull).
- Appended this section (append-only).
- Followed: branch-guard (stayed on chore/tero-index-cabal-ready), dev-workflow, signed commits.
- Landed: merge --no-ff chore → dev, push; dev → main --no-ff, push; propagate (dev pull main).
- Post: update-tero.sh py-rust-bridge; commit; ./scripts/check.sh ; tero re-query.
- Cross-cite: plan.md priority 1, dev-docs/waves/wsfull-wave-2026-07-09-compact.md, WORKSPACE_CABAL_TERO_READINESS.md.

Run `./scripts/check.sh` (or --fix/--quick) before PRs. Use cabal --use-tero from here.

Tero cite: agents--hygiene-tero-landing-chore-2026-07-09

## Semver + Releases (2026-07-10 appended, per user: toolchain/dev support first)

This is supportive tooling extracted from mycelium (read-only clone at /root/git/isolated/mycelium, perms 555 to prevent borking).
Language/project agnostic dev helper (py-rust bridge for porting/extraction).
Baseline v0.1.0 (no prior tags; versions unestablished).
Process: local build (uv/cargo), hygiene, append-only docs citing plan.md, tero, extraction (copy only), local podman GHCR (no Actions).
No mods to mycelium core (decomposed separately); only supportive easily-ported.

Cites: plan.md (semver writ large), user "starting with toolchain first and dev support", "only the tooling... in rust still... clone copy read only".
