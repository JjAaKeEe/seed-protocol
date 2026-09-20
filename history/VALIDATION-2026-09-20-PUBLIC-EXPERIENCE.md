# Validation report — Public Repository Experience Pass

**Date:** 2026-09-20  
**Branch:** `experience/public-repository-pass`  
**Validated local commit:** `b4f87ec` before this report  
**Experiment:** X-0003

## Outcome

The local repository passes structural, test, form, link, boot, and snapshot checks. The redesigned branch was not yet published when this report was written because the execution environment required an additional explicit approval for public branch egress. GitHub-rendered verification and pull-request checks therefore remain pending.

## Documentation and navigation

| Check | Result |
|---|---|
| README length | Pass — 1,774 words |
| Human entry | Pass — README routes to `START-HERE.md` |
| Agent entry | Pass — README routes to `AGENTS.md` and `BOOTSTRAP.md` |
| Beginner path | Pass structurally; no independent timed reader test yet |
| Expert path | Pass structurally through Questions, Challenges, model boundary, Decisions, and specification |
| Challenge entry | Pass — guide, index, form, and public Discussion exist |
| Quest entry | Pass — D1–D5, bounded examples, specialist routes, and Boss Problems exist |
| Local Markdown links | Pass — 0 broken local targets in repository Markdown |
| Mermaid accessibility | Pass by inspection — every new Mermaid diagram has an adjacent text alternative |
| GitHub-rendered Mermaid and anchors | Pending branch publication |

## GitHub community configuration

- Issues: enabled.
- Discussions: enabled.
- Eight issue forms parse as valid YAML.
- Blank issues are disabled; early conversation routes to Discussions.
- Existing categories are documented rather than destructively replaced.
- Three public Discussions were created:
  - [Welcome and first impressions](https://github.com/JjAaKeEe/seed-protocol/discussions/1)
  - [Attack the Seed](https://github.com/JjAaKeEe/seed-protocol/discussions/2)
  - [Contribution and Quest matching](https://github.com/JjAaKeEe/seed-protocol/discussions/3)
- Issue-form labels still require live-repository creation or confirmation after branch publication.

## Protocol and tooling

Command:

```sh
python3 tools/seed.py validate .
```

Result: `VALID`, 0 warnings.

Status output correctly reports `seed:S-0000`, maturity S2, executability E1, active state, and the updated license/public-experience state.

Boot packet generation completed successfully and produced a 31,704-byte routed context packet.

## Automated tests

```text
Ran 7 tests in 0.203s
OK
```

Covered behavior includes root validation, path containment, minimal initialization, boot routing, full Canon inclusion, missing required files, and portable snapshots.

## Portable snapshot

A clean ZIP snapshot was created at `/tmp/seed-protocol-experience-pass` for validation.

- 63 files
- 275,264 uncompressed bytes
- includes public docs, issue forms, license texts, Decisions, and X-0003
- excludes Git internals, Python caches, and AppleDouble metadata under existing snapshot rules

The `/tmp` artifact is disposable test output and is not part of the repository.

## Accessibility and language review

- Descriptive link text is used throughout new public routes.
- Meaning does not depend on color, badges, or icons.
- Defined protocol terminology is explained or routed to the vocabulary.
- GitHub-specific contribution terms are translated into plain language.
- Public claims remain adjacent to experimental limits and known Challenges.

Not yet empirically tested:

- screen-reader navigation;
- mobile GitHub rendering;
- comprehension by a teenager or unrelated newcomer;
- timed 30-second / 3-minute / 10-minute / 20-minute outcomes.

## Red-team disposition

The four-lens red team is recorded in X-0003. Its central unresolved finding is that the repository is now designed to receive independent criticism, but was authored and evaluated within the same workstream. Structural success is not user validation.

## Git and publication state

- Existing public history was preserved.
- Work is divided into coherent commits on `experience/public-repository-pass`.
- No published commits were rewritten.
- Branch push, rendered review, pull-request creation, and merge remain pending explicit external-publication approval.

## Release readiness

**Recommendation: do not publish a numbered `v0.1` release yet.**

The repository is suitable for an experimental public pull request. A numbered release should wait for:

1. merged and rendered verification on GitHub;
2. at least two independent agent cold-start runs from X-0001;
3. at least one timed human newcomer test;
4. one unlike reference Seed in addition to the planned Project Lithos;
5. confirmation that the dual-license boundary and issue-form choices are understandable;
6. an initial Canon stewardship policy.

## Final external checks after publication

1. Verify every Mermaid diagram, table, anchor, and relative link in GitHub’s rendered view.
2. Open the new-issue chooser and confirm all eight forms load and route correctly.
3. Create or confirm the labels referenced by issue forms.
4. Review pull-request diff and checks.
5. Merge only if the public branch contains no unintended or private material.
