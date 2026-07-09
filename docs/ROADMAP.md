# py-rust-bridge — Roadmap

**Status:** Scaffolding / hygiene (2026-07-09)  
**Role:** Thin support repo providing Python-Rust interoperability tools and FFI helpers (PyO3, binding gen, analysis).  
**Living with:** [README.md](../README.md) · [AGENTS.md](../AGENTS.md) · workspace [plan.md](../../plan.md)

Tero-ready (docs/tero-index) and hygiene (scripts/check.sh) added per plan.md priority 1 (hygiene-thin-repos).

## Waves (minimal for scaffolding)

### Wave H — Hygiene & Tero closure (this chore)
- Add scripts/check.sh modeled on search-box/cabal (uv if present, ruff/black, pytest, tero index gen)
- Minimal docs/ROADMAP.md (this) + AGENTS append
- Land chore/tero-index-cabal-ready → dev (merge --no-ff), → main; propagate
- update-tero; verify checks

### Wave P — Polish & Integration
- Full cabal-devmelopner + tero usage examples
- Rust side PyO3 examples / maturin support if expanded
- CI parity (pytest via uv)

See workspace plan.md §4 Thin Repos + Pending Branch Hygiene for context and dev-workflow.

Non-goals: full prod bridge (use maturin/pyo3 direct in consumers).

Tero cite this: use tero text_search "py-rust-bridge hygiene" after update.
