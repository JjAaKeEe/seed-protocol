# D-0008 — License software and knowledge separately

**Status:** accepted  
**Date:** 2026-09-20  
**Targets:** public contribution, reuse, Q-0042

## Context

The repository is publicly readable and now invites contribution. Leaving rights undecided makes legitimate reuse and contribution unnecessarily ambiguous. Software licenses and public-knowledge licenses solve different problems.

## Decision

- License software, executable tooling, tests, and reusable code under Apache License 2.0.
- License prose, documentation, specifications, descriptive data, diagrams, and media under Creative Commons Attribution 4.0 International unless an artifact declares otherwise.
- Explain the mapping in `LICENSE.md` and include both full license texts in `LICENSES/`.

## Alternatives considered

- Keep all rights reserved during public preview.
- Apply MIT to the entire repository.
- Apply CC BY 4.0 to everything.
- Use CC0 for data as a third default license.

## Consequences

- Public reuse and contribution have explicit defaults.
- Apache-2.0 provides software patent terms absent from MIT.
- CC BY 4.0 fits attribution-bearing intellectual work better than a software license.
- Mixed artifacts require judgment and occasionally an explicit declaration.
- The project must not imply that these licenses cover privacy, trademarks, or third-party material.

## Reconsider when

Revisit after legal review, when hardware designs or substantial datasets enter the corpus, if institutional contributors require a contributor agreement, or if the mixed-artifact boundary creates repeated confusion.
