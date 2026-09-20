# D-0001 — Separate Canon, Workspace, Evidence, and History

**Status:** accepted provisionally  
**Date:** 2026-09-20  
**Scope:** protocol semantics

## Context

Exploratory conversations and agent output easily blur current belief, speculation, supporting material, and the path by which conclusions changed. That makes polished drafts appear more certain than they are and permits transient workspace output to become authoritative accidentally.

## Decision

A mature Seed distinguishes four conceptual strata:

- **Canon:** accepted coordination state;
- **Workspace:** unaccepted exploration;
- **Evidence:** sources and observations;
- **History:** change, rationale, provenance, and failure.

The protocol does not require four literal directories. It requires the distinctions to remain discoverable.

## Alternatives considered

1. Treat the latest document as truth.
2. Treat the repository history as sufficient.
3. Use only status labels on individual paragraphs.
4. Store everything in one graph with typed relationships.

## Consequences

- Participants can be wrong without silently rewriting Canon.
- Evidence can be reinterpreted without being rewritten.
- Decision rationale and origin survive ordinary file diffs.
- The model adds classification effort and may become bureaucratic.

## Conditions for reconsideration

Revisit if applied Seeds cannot reliably classify material, if the distinctions require duplicate files, or if a simpler model preserves uncertainty and handoff equally well.

