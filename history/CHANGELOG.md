# Changelog

All notable accepted changes to Seed S-0000 are recorded here. This file is not a replacement for version-control history or Decision records.

## 2026-10-17 — Protocol drafts and license map

### Added

- Decision D-0009: template license fields stay `UNDECIDED`, the minimum Seed is the smallest that passes a cold start, Spark is a short working draft, and quests stay non-scored until C-0003 has evidence.
- `ROADMAP.md` stating pre-alpha limits. It does not claim a cold start has passed.
- `spec/SPARK-draft.md`, a working Spark draft, not frozen.
- Experiment kit `experiments/X-0001b-cold-start-testkit/`. The kit is drafted and has not been run.
- Decision D-0010 and the root `LICENSE` file (Apache-2.0 text) for software, specification text, and the manifest format.
- `LICENSE-docs` (CC BY 4.0) for explanatory documents.
- `TRADEMARK.md`, marked draft and not lawyer-reviewed. Accurate "conforms to Seed Protocol" wording is allowed. A "Seed-compatible" badge is reserved for Seeds that pass the reference validator. No badge has been issued.
- A `license_note` on the minimal template stating that license fields are `UNDECIDED` by design.

### Changed

- D-0004 is marked superseded by D-0008 and D-0009. The private-draft "all rights undecided" position is no longer the repository map.
- `LICENSE.md` now separates Apache-2.0 spec text and schemas from CC BY 4.0 explanatory docs, and states that template copies do not inherit either license.
- The normative draft now calls the current core file list a working structural form. The true minimum Seed is not established until a cold start passes.
- The constitutional shell's licensing section matches D-0010.

### Clarified

- The field ops product is separate, proprietary, and not in this repository.
- Lawyer review of the license map and trademark notice is still open.
- X-0001b does not mark the Seed bootable.

### Intentionally unresolved

- legal review;
- whether template files should later be dedicated to CC0;
- a published rule and artwork for any "Seed-compatible" badge;
- results of X-0001b, which has not been run;
- public governance and a numbered release.

## 2026-09-20 — Initial self-hosting draft

### Added

- machine-readable Seed manifest;
- human, agent, and Bootstrap entry points;
- canonical foundational Seed;
- constitutional principles;
- live status, model boundary, Questions, vocabulary, and authority policy;
- initial Decision and Challenge records;
- cold-start and cross-domain experiments;
- draft technical specification;
- minimal Seed template;
- zero-dependency reference CLI and test suite.
- explicit preservation and routing of the owner's 147-section founding charter.
- snapshot filtering for macOS AppleDouble metadata discovered on the target external volume.
- progressive public entry through `START-HERE.md` and focused guides for explanation, mechanics, Quests, Challenges, and design language;
- eight structured GitHub issue forms and a routed contribution experience;
- Apache-2.0 and CC BY 4.0 license texts with an explicit artifact mapping;
- Decisions D-0007 and D-0008 for public-experience architecture and dual licensing.
- Experiment X-0003, four-lens red-team findings, and a dated validation report.
- Public welcome, attack, and contribution-matching Discussions.

### Verified

- S-0000 passes structural validation in the selected repository.
- Seven reference tests pass on the external-volume installation.
- The first portable ZIP snapshot contains the founding charter and excludes Git internals, Python caches, and AppleDouble metadata.

### Clarified

- The founding charter is living R&D material. Its planted state is preserved by Git, but the document may be edited and reorganized deliberately.
- Repository state changed from private draft to public experimental; reuse licensing and contribution governance remain unresolved.
- `seed_golden_repo.md` is an intentionally incomplete constitutional shell and primary long-form build surface, not a finished or protected charter.
- The public README now exposes the thesis, limits, human/agent routes, attack surface, and contribution paths through progressive disclosure.

### Intentionally unresolved

- public name and brand;
- legal review of the mixed-artifact license mapping;
- governance;
- long-term public repository governance;
- external compatibility;
- Seed Commons product architecture.
