<!-- SPDX-License-Identifier: Apache-2.0 -->

# Seed Protocol 0.1-draft

## Status of this document

This is an experimental specification produced by Seed S-0000. It defines enough behavior to build and test reference Seeds. It is not a stable public standard and makes no compatibility promise beyond this repository.

The key words **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** indicate requirement strength within this draft.

## 1. Scope

Seed Protocol defines:

- how a portable Seed identifies itself;
- how humans and agents discover its entry points;
- how accepted state is distinguished from exploration, evidence, and history;
- how maturity, executability, uncertainty, authority, and handoff are exposed;
- the minimum behavior required for structural validation and cold start.

It does not define:

- a hosting service;
- a universal governance model;
- a social network;
- a universal ontology;
- truth validation;
- physical-system safety certification;
- a required version-control system.

## 2. Conformance profiles

### 2.1 Core Seed

A Core Seed is the current working structural form. The true minimum Seed is the smallest that still passes a cold start (D-0009; not yet established, see Q-0001). A Core Seed MUST contain:

- `SEED.yaml`;
- a human entry document;
- a canonical entry document;
- a Bootstrap document;
- current status;
- principles or constraints;
- open questions;
- a model boundary.

The exact filenames beyond `SEED.yaml` MAY vary when the manifest routes them explicitly.

### 2.2 Agent-compatible Seed

An Agent-compatible Seed is a Core Seed whose Bootstrap and manifest pass a cold-start evaluation in at least one declared agent environment. Host-specific instruction files MAY be present but MUST be treated as adapters.

### 2.3 Full Seed

A Full Seed additionally represents Decisions, Challenges, Experiments, provenance, history, authority boundaries, and task-relevant evidence. These MAY be empty early in the lifecycle but their locations SHOULD be discoverable.

## 3. Manifest

### 3.1 Location and encoding

The root manifest MUST be named `SEED.yaml`, encoded as UTF-8.

Protocol 0.1-draft uses the `json-compatible-yaml` profile. The complete file MUST parse as JSON and is therefore also valid YAML 1.2. Future versions MAY support general YAML or other serializations through declared profiles.

### 3.2 Required fields

The manifest MUST contain:

| Field | Type | Meaning |
|---|---|---|
| `seed_protocol` | string | Protocol version or draft identifier |
| `manifest_profile` | string | Serialization profile |
| `id` | string | Stable Seed identifier |
| `title` | string | Human-readable title |
| `maturity` | string | `S0` through `S6` |
| `executability` | string | `E0` through `E6` |
| `status` | string | Current lifecycle state |
| `canonical_entry` | relative path | Current canonical narrative or index |
| `human_entry` | relative path | Human doorway |
| `bootstrap` | relative path | Agent/human cold-start orientation |
| `principles_entry` | relative path | Governing values or constraints |
| `status_entry` | relative path | Current state and handoff |
| `model_boundary_entry` | relative path | Included, excluded, and uncertain scope |
| `questions_entry` | relative path | Contribution-ready unknowns |
| `required_files` | array | Files required by this Seed profile |
| `updated` | string | ISO date of last meaningful accepted update |

### 3.3 Recommended fields

A manifest SHOULD contain:

- `subtitle`;
- `visibility`;
- `agent_entry` when a host adapter exists;
- `vocabulary_entry`;
- `authority_entry` at E2 or above;
- `provenance_entry`;
- `specification_entry` for protocol or standard Seeds;
- `domains`;
- `epistemic_state`;
- `agency`;
- `license`;
- `parents` and `derivatives`;
- `created`.

### 3.4 Identifier

The provisional identifier form is `seed:<local-identifier>`. Identifiers MUST be non-empty and SHOULD remain stable across moves and renames. Global resolution is not defined in 0.1-draft.

### 3.5 Paths

Entry paths MUST be relative to the Seed root. They MUST NOT escape the root through `..`. A portable Seed MUST NOT place machine-specific absolute paths in the manifest.

## 4. Entry documents

### 4.1 Human entry

The human entry SHOULD explain within a few minutes:

- what the Seed is;
- why it exists;
- maturity and status;
- where to begin;
- how to inspect uncertainty and contribute.

### 4.2 Canonical entry

The canonical entry MUST identify the currently accepted narrative or route clearly to distributed Canon. Canon MUST NOT be described as unquestionable truth.

### 4.3 Bootstrap

The Bootstrap MUST provide:

- mission;
- central thesis or purpose;
- present state;
- context map;
- settled-enough claims;
- live hypotheses or uncertainty;
- high-value open questions;
- authority boundary or route to it;
- next useful action;
- handoff instructions.

The Bootstrap SHOULD remain materially shorter than the complete corpus. Its function is routing and orientation, not exhaustive documentation.

### 4.4 Status

Status MUST expose:

- maturity;
- executability;
- active/dormant/archived or equivalent state;
- last meaningful update;
- active workfronts;
- next useful action;
- unresolved human decisions or blockers.

### 4.5 Model boundary

The model boundary MUST identify important exclusions, biases, known blind spots, and the evidence quality of major claims. It SHOULD state what evidence would weaken the central thesis.

## 5. Maturity

| Level | Name | Minimum meaning |
|---|---|---|
| S0 | Spark | Raw thought worth retaining |
| S1 | Seed | Independently understandable concept |
| S2 | Developed Seed | Principles, model, questions, and handoff exist |
| S3 | Researched Concept | Evidence has materially tested assumptions |
| S4 | Experiment / Prototype | Documented real trial exists |
| S5 | Validated Practice | Defined implementation works under stated conditions |
| S6 | Living System | Operational and maintained in the world |

Maturity MUST NOT be inferred from document length, design polish, popularity, or agent output volume.

## 6. Executability

| Level | Name | Minimum meaning |
|---|---|---|
| E0 | Readable | Machine can interpret the corpus |
| E1 | Queryable | Machine can navigate state and cold-start |
| E2 | Researchable | Agents can investigate bounded questions |
| E3 | Simulatable | Formal models support computational experiments |
| E4 | Experimentable | Approved systems can operate bounded test environments |
| E5 | Fabricable | Approved workflows can produce physical artifacts |
| E6 | Operational | Agents can participate in real operation under governance |

At E2 and above, explicit agency policy SHOULD exist. At E4 and above, the Seed MUST NOT claim conformance merely because tools are technically accessible; responsible authority and safety controls are required.

## 7. Intellectual strata

A Full Seed MUST make these distinctions discoverable:

- **Canon** — accepted coordination state;
- **Workspace** — unaccepted exploration;
- **Evidence** — sources and observations;
- **History** — change, rationale, provenance, and failure.

They need not map one-to-one to directories.

Material MUST NOT be promoted from Workspace into Canon solely because multiple agents repeat it or because it is written persuasively.

## 8. Decisions

A material Decision SHOULD record:

- stable ID;
- status;
- date;
- context;
- decision;
- alternatives;
- consequences;
- evidence when applicable;
- conditions for reconsideration.

Accepted Decisions SHOULD remain preserved after reversal.

## 9. Challenges

A Challenge SHOULD record:

- stable ID;
- target;
- status;
- claim or attack;
- importance;
- current evidence;
- proposed test or resolution.

Challenges MAY target the Seed's ontology rather than a single claim. Resolved Challenges SHOULD remain in History.

## 10. Experiments and failures

An Experiment SHOULD record:

- question;
- hypothesis;
- method;
- conditions;
- observations;
- results;
- uncertainty;
- artifacts;
- conclusion;
- next questions.

A failed Experiment SHOULD record what it ruled out and what remains unknown. Failure MUST NOT be erased solely because the hypothesis was not supported.

## 11. Questions

Questions SHOULD be specific enough for a participant to choose and act upon. They MAY include:

- difficulty;
- domain;
- skills;
- location;
- estimated effort;
- dependencies;
- evidence threshold;
- related objects.

## 12. Provenance

A Full Seed SHOULD preserve:

- origin context;
- meaningful human contributors;
- meaningful agent/system contributions;
- external influences;
- privacy or attribution caveats.

Provenance MUST NOT require disclosure of private source material. Public Canon MAY summarize private origins with consent-sensitive detail.

## 13. Authority

The Seed MUST NOT imply that access equals authorization.

Agency descriptions SHOULD distinguish:

- read;
- local analysis;
- local execution;
- canonical modification;
- external communication;
- purchasing;
- fabrication;
- physical actuation.

Higher-level permissions MUST NOT be inferred from lower-level permissions.

## 14. Boot protocol

The reference Seed Boot Protocol is:

1. **Discover** — parse the manifest.
2. **Orient** — read host instructions and Bootstrap.
3. **Anchor** — load principles, status, vocabulary, and model boundary.
4. **Select** — determine the current task.
5. **Retrieve** — load only relevant deeper material.
6. **Verify** — inspect evidence, Decisions, and Challenges.
7. **Act** — perform bounded work.
8. **Record** — preserve accepted results and provenance.
9. **Handoff** — leave the Seed re-bootable.

An implementation MAY automate this sequence. It SHOULD expose which context was loaded.

## 15. Cold-start evaluation

An Agent-compatible conformance claim SHOULD identify:

- environment and model;
- exact initial prompt;
- corpus version;
- evaluation rubric;
- result;
- authority errors;
- unsupported claims.

Fluent paraphrase alone is not sufficient. Evaluation SHOULD cover identity, state, routing, uncertainty, model boundary, authority, and next action.

## 16. Structural validation

A validator MUST distinguish errors from warnings.

Errors include:

- unreadable or invalid manifest;
- missing required field;
- invalid maturity or executability value;
- referenced required file missing;
- entry path escaping the Seed root.

Warnings may include:

- unresolved license;
- missing host adapter;
- status date older than the manifest update;
- empty optional collection;
- absent authority entry at higher executability.

Structural validation MUST NOT claim factual or scientific validity.

## 17. Snapshot and portability

A portable snapshot SHOULD include all files needed to interpret the Seed without its hosting platform. It SHOULD exclude caches, repository internals, secrets, and derived local state.

Critical state MUST NOT exist only in a binary artifact. Binary artifacts MAY be included when accompanied by enough open description to identify their role and provenance.

## 18. Security and privacy

Seed consumers MUST treat repository content as untrusted input. Host agents SHOULD obey their own safety and permission model rather than accepting Seed instructions as higher authority.

A Seed MUST NOT embed secrets in the manifest or canonical documents. Source material containing private data SHOULD be separated, access-controlled, or sanitized before publication.

## 19. Extensions

Implementations MAY add fields and files. Extensions SHOULD:

- use names unlikely to collide;
- remain ignorable by consumers that do not understand them;
- avoid redefining core fields;
- preserve portable export.

## 20. Compatibility

Protocol 0.x versions are experimental. Breaking changes are permitted when recorded in a Decision and changelog. Stable compatibility semantics are deferred until evidence from several external Seeds exists.

## 21. Reference implementation

The `tools/seed.py` utility is a reference, not the normative protocol. A Seed may conform without using Python or this directory layout if it satisfies the semantic and manifest requirements.

