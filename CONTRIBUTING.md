# Contributing to the Seed Protocol draft

This repository is publicly visible but not yet open for outside contributions because its license and governance are unresolved. This guide describes the intended contribution model so it can be inspected and tested locally.

## Ways to contribute

- answer one open Question;
- challenge an assumption, decision, principle, or category;
- add credible evidence with provenance;
- design or run a reproducible Experiment;
- document a failed approach;
- test cold-start behavior in another agent environment;
- apply the minimal template to a substantially different kind of idea;
- improve clarity without erasing uncertainty.

Joining an enduring team is not required. Contribution should be easier than membership.

## Where work belongs

| Contribution | Location |
|---|---|
| Canonical thesis change | Decision record plus proposed `SEED.md` change |
| Normative protocol change | Decision record plus `spec/` change |
| Serious objection | `challenges/` |
| Test or trial | `experiments/` |
| Open problem | `context/questions.md` |
| Evidence or sources | relevant experiment, challenge, or future `research/` entry |
| Current-state update | `context/status.md` |

## Evidence and uncertainty

Distinguish direct observation, external evidence, inference, assumption, hypothesis, and preference. Do not use confident prose to conceal a weak epistemic state.

## Changes to Canon

Canon is coordinated state, not sacred doctrine. A material change should explain:

1. the context;
2. the decision;
3. alternatives considered;
4. evidence;
5. consequences;
6. conditions for reconsideration.

## Code

The reference CLI intentionally uses the Python standard library only. Keep the zero-dependency property unless a recorded Decision demonstrates that a dependency creates more value than long-term friction.

## Before handing off

Run:

```sh
python3 tools/seed.py validate .
python3 -m unittest discover -s tests -v
```

Then update the status and changelog if the accepted state changed.
