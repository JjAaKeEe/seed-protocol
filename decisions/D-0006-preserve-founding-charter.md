# D-0006 — Version the living founding charter beside distilled Canon

**Status:** accepted  
**Date:** 2026-09-20  
**Scope:** provenance, source material, Canon

## Context

The owner placed `seed_golden_repo.md` in the repository directory. It is the complete 147-section standalone document developed before implementation. The new self-hosting corpus distills the same thinking into routed context, normative specification, Decisions, Challenges, and executable tests.

Replacing the charter with the distilled version would save space but violate the protocol's own concern that compression can erase human meaning. Treating the charter as frozen would prevent useful R&D. Treating it as current Canon would make cold start expensive and blur origin with accepted implementation.

## Decision

Keep `seed_golden_repo.md` at the repository root as the living founding charter and declared origin source. Preserve its planted form through the initial Git commit, then allow deliberate edits during R&D.

- `seed_golden_repo.md` is the evolving source-of-origin charter.
- `SEED.md` is the current canonical synthesis.
- `spec/seed-protocol-v0.1-draft.md` is the normative technical draft.
- Decisions record why implementation departs from or narrows the charter.

Material charter changes SHOULD be visible in Git history and SHOULD update relevant Decisions when they alter protocol doctrine.

## Consequences

- Original intent remains recoverable through history while the charter can improve.
- Agents can inspect deeper context when a distilled principle is ambiguous.
- The repository carries some deliberate duplication.
- Readers must understand that source-of-origin is not automatically current truth.

## Conditions for reconsideration

The charter may be split, renamed, or moved after stable references and migration tooling exist. History must retain the planted version. Redaction still requires explicit owner review when privacy or publication concerns arise.
