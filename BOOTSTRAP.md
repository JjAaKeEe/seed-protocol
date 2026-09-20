# Bootstrap — Seed S-0000

## 1. Mission

Define and test the smallest portable structure that can turn a human idea into a durable intellectual object: understandable to people, deterministically bootable by capable agents, explicit about uncertainty and authority, open to attack and derivation, capable of dormancy, and independent of any single platform.

## 2. Central thesis

> A Seed is a portable unit of human intent and structured knowledge capable of being understood, challenged, extended, and eventually executed by humans and intelligent systems without requiring continued access to its original creator or originating conversation.

The strongest future form is not merely a document. It is an initiation state from which a bounded human-machine research and development ecology may be instantiated.

## 3. Present state

- The conceptual doctrine is developed enough to test.
- The protocol is an experimental `0.1-draft`, not a standard.
- This repository is the first self-hosting reference Seed.
- The manifest, bootstrap, context layers, decision/challenge records, minimal template, and reference CLI now exist.
- No external compatibility claims have been validated.
- No license has been selected.
- No public community or Seed Commons platform exists.
- Project Lithos is the planned first complex external reference Seed.

## 4. Constitutional center

Do not collapse these commitments:

1. Human-readable and machine-bootable are equal requirements.
2. The protocol is platform-independent; Git and `AGENTS.md` are adapters.
3. Canon, Workspace, Evidence, and History are distinct.
4. Conversation is source material, not canonical state.
5. A polished claim is not a validated claim.
6. Challenge, falsification, and failure are valuable contributions.
7. Dormancy is legitimate; reactivation must be cheap.
8. Contribution should be easier than membership.
9. Motivation should create purpose and mastery, not compulsion.
10. Permission to reason never implies permission to act in the world.
11. Seeds should remain forkable and transferable.
12. The Seed has no inherent right to survive a better model.

The full constitution is in `context/principles.md`.

## 5. Context map

Load in this order unless the task clearly requires another path:

| Need | Read |
|---|---|
| Identity and routing | `SEED.yaml` |
| Canonical thesis | `SEED.md` |
| Governing commitments | `context/principles.md` |
| Live work and handoff | `context/status.md` |
| What the model excludes | `context/model-boundary.md` |
| Terms and distinctions | `context/vocabulary.md` |
| Unresolved work | `context/questions.md` |
| Permission boundaries | `context/authority.md` |
| Normative requirements | `spec/seed-protocol-v0.1-draft.md` |
| Why a choice was made | matching file in `decisions/` |
| Serious objections | matching file in `challenges/` |
| Test evidence | matching file in `experiments/` |
| Origin and attribution | `history/PROVENANCE.md` |
| Expandable constitutional shell and full corpus | `seed_golden_repo.md` |

## 6. Known enough to rely upon

- A Seed requires an explicit identity, human entry, canonical entry, bootstrap path, and current status.
- Layered context is preferable to a monolithic prompt or archive dump.
- Version history alone cannot preserve decision rationale or intellectual provenance.
- Agent orientation and agent authority are separate concerns.
- A protocol implementation must remain readable when its preferred application is unavailable.
- Challenge objects and reversal conditions prevent Canon from hardening into dogma.
- Real usage should determine later ontology and platform design.
- The constitutional shell is intentionally incomplete and is expected to grow into the exhaustive long-form corpus.
- Its Git history remains a check against meaning lost during rewriting or distillation.

## 7. Live hypotheses

These are plausible, not established:

- One general Seed grammar can serve engineering, creative, institutional, research, and software ideas without becoming vague or bureaucratic.
- A short bootstrap plus routed context can orient an unfamiliar agent more reliably than a single large canonical document.
- Plain files plus Git are sufficient for early collaboration and protocol research.
- Structured Challenges will improve truth-seeking instead of becoming administrative theater.
- Purpose matching and calibrated quests can attract useful expertise without degrading into engagement optimization.
- A Seed can eventually act as an executable initiation state for bounded agent ecosystems.

## 8. Highest-value open questions

1. What is the true minimum Seed, and which fields are merely attractive ceremony?
2. Can three unrelated Seed types use the same core without distortion?
3. What information must always be loaded, and what can be retrieved only for a task?
4. How should a cold-start test measure accurate orientation rather than eloquent paraphrase?
5. How are Canon changes governed without requiring one universal political model?
6. How should evidence, confidence, and provenance be represented without false precision?
7. How can the protocol remain useful outside Git and outside coding-agent ecosystems?
8. When do motivational mechanics improve contribution, and when do they corrupt it?
9. How are machine permissions inherited, narrowed, audited, and revoked at higher executability levels?

See `context/questions.md` for the working queue.

## 9. Authority boundary

This Seed authorizes reading and local analysis. It does not itself authorize publication, external communication, purchases, public licensing, fabrication, or physical actuation. User instructions and the active execution environment determine those permissions. See `context/authority.md`.

## 10. Current workfront

The present workfront is protocol falsification through use:

1. validate S-0000 structurally;
2. cold-start unfamiliar agents from the corpus;
3. convert Project Lithos as the first complex reference Seed;
4. convert a very different small Seed;
5. record friction as evidence;
6. revise the protocol only where repeated friction justifies it.

## 11. Do not build yet

Do not start with a social network, universal ontology, graph database, vector layer, reputation economy, agent marketplace, complex permission service, token system, or polished web platform. These are hypotheses about future needs, not present requirements.

## 12. Handoff

If you are resuming after dormancy, run:

```sh
python3 tools/seed.py validate .
python3 tools/seed.py status .
python3 tools/seed.py boot .
python3 -m unittest discover -s tests -v
```

Then inspect the most recent entry in `history/CHANGELOG.md`. Choose one open question or experiment. Record substantive outcomes in the Seed rather than leaving them only in conversation.
