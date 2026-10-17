# D-0006 — Develop the constitutional shell beside distilled Canon

**Status:** accepted  
**Date:** 2026-09-20  
**Scope:** provenance, source material, Canon

## Context

The owner placed `seed_golden_repo.md` in the repository directory as a 147-section shell. It contains the originating structure and substantial initial text, but it was always intended to be populated and built out completely through R&D. The self-hosting corpus also distills the work into routed context, normative specification, Decisions, Challenges, and executable tests.

Replacing the shell with the distilled version would save space but violate the protocol's own concern that compression can erase human meaning. Treating the shell as a completed or protected artifact would defeat its purpose. Treating every exploratory expansion as current Canon would make cold start expensive and blur R&D with accepted implementation.

## Decision

Keep `seed_golden_repo.md` at the repository root as the expandable constitutional shell, full design corpus, and declared origin source. Preserve its planted form through Git history, then develop it directly during R&D.

- `seed_golden_repo.md` is the evolving long-form constitution.
- `SEED.md` is the current canonical synthesis.
- `spec/seed-protocol-v0.1-draft.md` is the normative technical draft.
- Decisions record why implementation departs from or narrows the charter.

The shell MAY be populated section by section, substantially rewritten, illustrated with diagrams and charts, reorganized, split into routed subdocuments, and extended with new sections. Material doctrinal changes SHOULD be visible in Git history and SHOULD update relevant Decisions, concise Canon, or the specification when appropriate.

## Consequences

- Original intent remains recoverable through history while the constitution grows.
- Agents can inspect deeper context when a distilled principle is ambiguous.
- The repository carries deliberate layering between exhaustive exploration, concise Canon, and normative specification.
- Readers must understand that source-of-origin is not automatically current truth.

## Conditions for reconsideration

The shell may be split, renamed, or moved whenever doing so improves authoring and bootload, provided references migrate cleanly and history retains the planted version. Redaction still requires explicit owner review when privacy or publication concerns arise.
