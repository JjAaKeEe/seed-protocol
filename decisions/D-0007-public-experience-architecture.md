# D-0007 — Use progressive dual-entry public architecture

**Status:** accepted  
**Date:** 2026-09-20  
**Targets:** public repository experience, P-01, P-02, P-09, P-11

## Context

The original repository was structurally coherent but presented protocol internals before giving unfamiliar readers a reason to care or a safe action to take. A single README was serving newcomers, experts, contributors, and agents poorly.

## Decision

Use progressive disclosure with two visible entry paths:

- humans enter through `START-HERE.md` and task-specific explanatory documents;
- agents enter through `AGENTS.md` and `BOOTSTRAP.md`.

Keep `README.md` as the shared public front door. Treat reader-path documents, GitHub forms, Quests, and Discussions as adapters rather than required Seed Protocol core objects.

Design for four outcomes: curiosity in 30 seconds, comprehension in 3 minutes, traction in 10 minutes, and a contribution route in 20 minutes.

## Alternatives considered

- Put every audience in one exhaustive README.
- Build a documentation website.
- Make the specification the primary entry.
- Use separate repositories for human and agent documentation.

## Consequences

- Public entry becomes easier without changing the boot contract.
- Some explanatory duplication is deliberate.
- Navigation and canonical-source labels must be maintained.
- The repository can test its experience before committing to a web platform.

## Reconsider when

Revisit if cold-start or reader testing shows that multiple paths create drift or confusion, if GitHub rendering becomes a material limit, or if a smaller architecture performs as well across unlike Seeds.

