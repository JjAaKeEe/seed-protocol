# D-0010 — Spec and schemas under Apache-2.0; docs under CC BY 4.0

**Status:** accepted as the repository map (owner instruction, 2026-10-17). Lawyer review is still open. This record is not legal advice.  
**Date:** 2026-10-17  
**Targets:** D-0004, D-0008, D-0009, Q-0042

## Context

D-0008 licensed software under Apache-2.0 and put specifications with the CC BY 4.0 knowledge set. D-0009 kept template-created Seeds at `UNDECIDED` and deferred a root `LICENSE` file and the D-0004 supersession until the owner revisited the commercial boundary. The owner instructed that revisit: the open protocol stays permissive, and the field ops product stays a separate proprietary codebase that is not in this repository.

## Decision

- License normative specification text and the manifest format it defines (`spec/`, including `spec/SPARK-draft.md`) under Apache-2.0, together with `tools/seed.py`, `tests/`, and other software. The root `LICENSE` file is the standard Apache-2.0 text.
- Keep explanatory documents under CC BY 4.0, as D-0008 decided for knowledge and media. The text is in `LICENSE-docs`.
- Template files carry no license-grant strings. A Seed created from `templates/` keeps every license field `UNDECIDED` until its author chooses (D-0009). Content written into that Seed does not inherit Apache-2.0 or CC BY 4.0 from this repository.
- Mark D-0004 superseded by D-0008 and D-0009. This decision refines D-0008's map; it does not replace D-0009's template rule.
- Add `TRADEMARK.md` as a draft. Accurate "conforms to Seed Protocol" statements are allowed. A "Seed-compatible" badge is reserved for Seeds that pass the reference validator. No badge has been issued.
- State in `LICENSE.md` that the field ops product is separate, proprietary, and not in this repository.

## Alternatives considered

- Leave specifications under CC BY 4.0, as D-0008 first wrote.
- Dedicate template files to CC0 in this change.
- Put a restrictive license on the protocol in order to protect the field ops product.

## Consequences

- A host that detects a single repository license can see Apache-2.0 from the root `LICENSE` file. `LICENSE.md` remains the artifact map, because one detected license does not describe the CC BY documents or the `UNDECIDED` template default.
- The protocol license is not a product license. Nothing in this repository is the field ops product.
- Lawyer review is still required before treating this map as cleared for investors, paid pilots, or a trademark filing.
- No conformance claim in this decision has been tested by X-0001b. Structural validation and the unit tests are the checks this repository can currently run.

## Reconsider when

Revisit after lawyer review, before any relicensing, if hardware designs or a contributor agreement are added, or if the template boundary is misunderstood in practice.
