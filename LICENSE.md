# Licensing

Seed Protocol contains different kinds of work. The applicable license follows the artifact. The root `LICENSE` file is the Apache License 2.0 text so a host can detect a license. It does not by itself license every file. This page is the map. It is an owner instruction recorded in D-0008, D-0009, and D-0010. It has not had lawyer review and is not legal advice.

D-0004 (all categories `UNDECIDED` for the private draft) is superseded by D-0008 and D-0009.

## Software, specification text, and schemas — Apache License 2.0

Licensed under the [Apache License 2.0](LICENSE). A copy is also stored at [LICENSES/Apache-2.0.txt](LICENSES/Apache-2.0.txt).

This includes:

- `tools/seed.py` and other software under `tools/`;
- `tests/`;
- normative specification text under `spec/`, including `spec/SPARK-draft.md` and `spec/seed-protocol-v0.1-draft.md`;
- the manifest format those specifications define (the schema for `SEED.yaml`).

SPDX identifier: `Apache-2.0`

Apache-2.0 does not grant trademark rights. See [TRADEMARK.md](TRADEMARK.md), which is a draft and needs lawyer review.

## Explanatory documents — Creative Commons Attribution 4.0

Prose that explains the project, diagrams, research records, and media are licensed under the [Creative Commons Attribution 4.0 International license](LICENSE-docs), unless an artifact declares another license. A copy of the CC BY 4.0 text is also stored at [LICENSES/CC-BY-4.0.txt](LICENSES/CC-BY-4.0.txt).

This includes:

- `README.md`, `START-HERE.md`, `CONTRIBUTING.md`, `AGENTS.md`, `BOOTSTRAP.md`, `SEED.md`, `ROADMAP.md`, and `seed_golden_repo.md`;
- `context/`, `decisions/`, `challenges/`, `experiments/`, `history/`, and `docs/`;
- diagrams and other media.

SPDX identifier: `CC-BY-4.0`

Suggested attribution:

> “Seed Protocol,” Seed S-0000 contributors, licensed under CC BY 4.0, with a link to the source and an indication of changes.

Git history is the primary contributor-attribution record. Individual artifacts may include more specific provenance.

## Templates — no license strings on contributed Seeds

Files under `templates/` carry no license-grant header. Copying a template does not place the new Seed under Apache-2.0 or CC BY 4.0.

A Seed created from the template keeps its own license fields at `UNDECIDED` until the author of that Seed chooses (D-0009). Ideas contributed in those Seeds do not inherit the licenses of this repository. This page does not dedicate the template files to CC0; that dedication has not been made.

## What is not in this repository

The field ops product is a separate proprietary product. It is not in this repository. Nothing in `LICENSE`, `LICENSE-docs`, or this map licenses that product.

## Other limits

Third-party material remains under its original terms and must be identified near the artifact. No repository license overrides third-party rights, privacy obligations, trademarks, patents not covered by Apache-2.0, or permissions the contributor did not possess.

When a file contains both explanatory prose and reusable code, the code is offered under Apache-2.0 and the surrounding explanation under CC BY 4.0. If that distinction is impractical, open an issue so the artifact can declare one license.

## Contributions

Unless explicitly agreed otherwise before acceptance, contributions are licensed under the license applicable to the area they modify. Contributors retain copyright and provide the permissions described by that license. A contribution that only fills in a separate Seed does not grant this repository rights in that Seed.

This mapping should receive legal review before institutional adoption, investor diligence, paid pilots, or the acceptance of materially complex third-party assets.
