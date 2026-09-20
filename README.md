# Seed Protocol — S-0000 “The Golden Seed”

> A portable unit of human intent that people and intelligent agents can understand, challenge, extend, and hand onward without requiring its creator or originating conversation.

**Status:** experimental foundation  
**Maturity:** S2 — Developed Seed  
**Machine executability:** E1 — Queryable and agent-bootable  
**Protocol version:** 0.1-draft

This repository is both:

1. the first implementation of Seed Protocol; and
2. the Seed that defines Seed Protocol.

That recursion is deliberate. The protocol must prove it can represent itself before it asks other ideas to use it.

The original 147-section founding charter lives in [`seed_golden_repo.md`](seed_golden_repo.md). It is the source-of-origin and a living R&D document, not disposable scaffolding or immutable scripture. Git history preserves earlier forms while the charter, `SEED.md`, and the specification evolve for different purposes.

## Why this exists

Interesting ideas emerge in conversation, work, journals, field observations, sketches, and AI sessions. Most are either forced prematurely into projects or allowed to disappear. Seed Protocol creates a third path: develop an idea only far enough that it becomes durable, legible, challengeable, and transferable.

A Seed is not necessarily a company, repo, paper, specification, or project. It is the persistent intellectual chassis beneath any of those forms.

## Begin here

For a human:

1. Read [SEED.md](SEED.md) for the canonical concept.
2. Read [context/principles.md](context/principles.md) for the constitutional commitments.
3. Read [context/status.md](context/status.md) for the live state and next work.
4. Read [context/questions.md](context/questions.md) to find useful unresolved problems.

For an AI agent:

1. Read [SEED.yaml](SEED.yaml).
2. Follow [AGENTS.md](AGENTS.md).
3. Execute the orientation sequence in [BOOTSTRAP.md](BOOTSTRAP.md).
4. Load only task-relevant deeper context.
5. Leave the Seed at least as bootable as you found it.

## Core model

Every mature Seed separates four strata:

| Stratum | Purpose |
|---|---|
| **Canon** | The currently accepted state from which work proceeds. Canon is authoritative, not infallible. |
| **Workspace** | Drafts, branches, hypotheses, proposed changes, and other places where participants may be wrong safely. |
| **Evidence** | Sources, observations, experiments, calculations, simulations, and artifacts. |
| **History** | Version change, decision rationale, intellectual provenance, rejected paths, and failures. |

Seed Protocol also treats Questions, Decisions, Challenges, Experiments, and Failures as durable objects. A useful attack on the Seed can be more valuable than support for it.

## Repository map

```text
seed-protocol/
├── README.md                 human doorway
├── SEED.yaml                 machine-readable passport
├── AGENTS.md                 compatibility doorway for coding agents
├── BOOTSTRAP.md              deterministic orientation sequence
├── SEED.md                   canonical thesis and conceptual architecture
├── seed_golden_repo.md       living founding charter / origin source
├── context/                  principles, state, boundaries, questions, terms
├── decisions/                accepted choices and reversal conditions
├── challenges/               persistent attacks on the Seed
├── experiments/              tests and their evidence
├── spec/                     normative draft specification
├── templates/minimal-seed/   smallest practical reusable Seed
├── tools/seed.py             zero-dependency reference CLI
├── tests/                    executable protocol checks
└── history/                  changelog and provenance
```

## Try the reference implementation

No third-party Python packages are required.

```sh
python3 tools/seed.py validate .
python3 tools/seed.py status .
python3 tools/seed.py boot .
python3 -m unittest discover -s tests -v
```

Create a new local Seed from the minimal template:

```sh
python3 tools/seed.py init ../my-seed --id seed:my-seed --title "My Seed"
```

Create a durable ZIP snapshot:

```sh
python3 tools/seed.py snapshot .
```

## What this draft intentionally does not build

This repository does not yet contain a social network, knowledge graph, vector database, reputation economy, agent marketplace, token system, or polished web application. Those may eventually become useful. Building them before the Seed object survives real use would freeze guesses into infrastructure.

The immediate experiment is smaller: can unfamiliar humans and agents cold-start the same idea, understand its uncertainty and authority boundaries, contribute without creator assistance, and leave a better handoff?

## Safety and authority

A Seed can describe action without authorizing action. Research permission never implies permission to purchase, communicate externally, fabricate, operate equipment, or affect a physical system. See [context/authority.md](context/authority.md).

## Licensing

Licensing is deliberately unresolved in this private draft. No public contribution should be solicited until documentation, software, data, and media licenses are chosen explicitly. See [LICENSE.md](LICENSE.md) and [decisions/D-0004-licensing-remains-open.md](decisions/D-0004-licensing-remains-open.md).

## The present test

The next important act is not to expand this doctrine. It is to attack it with real Seeds. Project Lithos is the likely first complex reference case; a sharply different creative or software Seed should follow so the protocol does not overfit research-heavy systems thinking.
