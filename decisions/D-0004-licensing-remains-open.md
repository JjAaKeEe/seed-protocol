# D-0004 — Keep licensing unresolved in the private draft

**Status:** superseded by D-0008 and D-0009 on 2026-10-17  
**Date:** 2026-09-20  
**Scope:** rights and publication

## Supersession

D-0008 chose Apache-2.0 for software and CC BY 4.0 for explanatory knowledge and media in this repository. D-0009 keeps Seeds created from `templates/` at `UNDECIDED`, so a contributed idea does not inherit those licenses. D-0010 refines the D-0008 map: spec text and the manifest format are Apache-2.0, the root `LICENSE` and `LICENSE-docs` files exist, and lawyer review is still open. The text below is the private-draft position this decision recorded. It is not the current map.

## Context

The intended ecosystem favors reuse and collaboration, but a Seed may contain prose, software, data, hardware designs, and media with different licensing needs. Selecting a license is a meaningful legal and strategic choice for the owner. The present work occurs in a private draft and the owner has not made that choice explicitly.

## Decision

Record all license categories as `UNDECIDED`. Do not solicit public contributions or imply open-source permissions until the owner chooses licenses.

## Alternatives considered

- CC BY 4.0 for everything;
- Apache-2.0 for everything;
- a mixed CC BY / Apache / CERN-OHL arrangement;
- public domain dedication.

## Consequences

- No important rights decision is made silently.
- The repository is not ready for public collaboration.
- A licensing decision becomes a release gate.

## Conditions for reconsideration

Resolve before first public publication or external contribution. Obtain legal advice if hardware, patent-sensitive material, or commercial implementations make the choice consequential.

