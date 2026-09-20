# D-0005 — Treat AGENTS.md as an adapter, not the protocol

**Status:** accepted provisionally  
**Date:** 2026-09-20  
**Scope:** agent interoperability

## Context

Several coding-agent environments can discover repository instructions, and `AGENTS.md` is a useful current convention. Making it normative would couple the protocol to one ecosystem and confuse behavioral instructions with portable Seed semantics.

## Decision

Use `AGENTS.md` as the first compatibility adapter. The portable contract remains the manifest plus Bootstrap and Canon entries. Future hosts may use other adapters.

## Consequences

- Current agents receive immediate guidance.
- The corpus remains conceptually portable.
- Multiple adapters may eventually need maintenance.

## Conditions for reconsideration

Revisit if a broadly adopted standard provides equivalent boot discovery, or if adapter drift proves too costly.

