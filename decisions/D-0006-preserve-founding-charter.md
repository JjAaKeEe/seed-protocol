# D-0006 — Preserve the founding charter beside distilled Canon

**Status:** accepted  
**Date:** 2026-09-20  
**Scope:** provenance, source material, Canon

## Context

The owner placed `seed_golden_repo.md` in the repository directory. It is the complete 147-section standalone document developed before implementation. The new self-hosting corpus distills the same thinking into routed context, normative specification, Decisions, Challenges, and executable tests.

Replacing the charter with the distilled version would save space but violate the protocol's own concern that compression can erase human meaning. Treating the charter as current Canon would make cold start expensive and blur origin with accepted implementation.

## Decision

Preserve `seed_golden_repo.md` verbatim at the repository root as the founding charter and declared origin source.

- `seed_golden_repo.md` is the source-of-origin.
- `SEED.md` is the current canonical synthesis.
- `spec/seed-protocol-v0.1-draft.md` is the normative technical draft.
- Decisions record why implementation departs from or narrows the charter.

Ordinary Canon work MUST NOT rewrite the founding charter.

## Consequences

- The original intent survives future compression and refactoring.
- Agents can inspect deeper context when a distilled principle is ambiguous.
- The repository carries some deliberate duplication.
- Readers must understand that source-of-origin is not automatically current truth.

## Conditions for reconsideration

The file may move into a dedicated source archive after stable references and snapshotting exist, but its content should remain preserved. Redaction requires explicit owner review if privacy or publication concerns arise.

