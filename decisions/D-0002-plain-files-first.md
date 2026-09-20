# D-0002 — Use plain files before platform infrastructure

**Status:** accepted provisionally  
**Date:** 2026-09-20  
**Scope:** reference implementation

## Context

The long-term vision could justify databases, semantic graphs, vector search, social features, agent services, and custom interfaces. The ontology and user behavior remain untested. Building a platform now would turn speculative structure into expensive commitments.

## Decision

The first reference implementation uses ordinary UTF-8 files, portable directory structure, a zero-dependency command-line tool, and optional Git history.

## Alternatives considered

- start with a hosted collaborative application;
- build a graph database as the source of truth;
- use a proprietary notes system;
- implement only a prose specification with no executable checks.

## Consequences

- The corpus remains inspectable and archive-friendly.
- Cold-start and portability can be tested immediately.
- Nontechnical creation remains less friendly than the eventual goal.
- Rich relationships are represented informally at first.

## Conditions for reconsideration

Introduce infrastructure when repeated use demonstrates a need that cannot be satisfied without disproportionate manual burden. New systems must retain complete portable export.

