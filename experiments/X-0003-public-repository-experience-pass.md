# X-0003 — Public Repository Experience Pass

**Status:** completed internally; external reader testing remains open  
**Date:** 2026-09-20  
**Questions:** Q-0001, Q-0010, Q-0032  
**Decisions:** D-0007, D-0008

## Baseline

The initial public repository was structurally coherent and agent-routable, but its main entry moved too quickly into protocol internals. It did not provide distinct beginner and expert paths, a visible Challenge index, contribution routes without Git, structured public forms, or an explicit reuse license.

## Hypothesis

A progressive, dual-entry repository can preserve protocol depth while allowing an unfamiliar reader to reach four outcomes:

| Time | Target |
|---|---|
| 30 seconds | Accurate curiosity |
| 3 minutes | Basic comprehension |
| 10 minutes | Traction into the relevant layer |
| 20 minutes | A safe and useful contribution path |

## Method

1. Preserve the existing boot contract and constitutional structure.
2. Build a shared README with separate Human Entry and Agent Entry routes.
3. Add focused explanatory, attack, Quest, community, and design-language documents.
4. Replace generic contribution guidance with persona-based paths.
5. Add structured issue forms and seed initial Discussions.
6. Make experimental status, model boundaries, and serious Challenges prominent.
7. Red-team the result from four perspectives.
8. Run structural, link, form, test, snapshot, and GitHub-rendering checks.

## Success criteria

- README remains between roughly 1,500 and 3,000 words.
- A newcomer can find a plain-language explanation and non-code contribution.
- An expert can locate questions, assumptions, evidence needs, and Challenges.
- An agent can retain the existing deterministic boot route.
- Human and agent entry paths converge on the same Canon without pretending to be identical.
- Challenge receives comparable prominence to expansion.
- GitHub issue forms parse and route unformed conversation toward Discussions.
- Licensing is explicit by artifact class.
- CLI validation and all reference tests continue to pass.

## Implementation observations

- Six focused reader documents were enough to create progressive disclosure without a documentation framework.
- The README reached 1,774 words: substantial but within the intended range.
- Mermaid diagrams work as relationship maps only when accompanied by text alternatives.
- The existing Question IDs already supported a Quest layer; no new protocol object was required.
- Existing GitHub Discussion categories were sufficient when paired with a repository-specific category map.
- Public contribution made the previously undecided license state untenable; this produced D-0008.
- The constitutional shell benefited from targeted expansion without attempting to complete unrelated sections.

## Four-lens red team

### Beginner

**What improved:** A reader can start with one sentence, one example, a route table, and a D1 contribution. GitHub terminology is explained. No local setup is required.

**Remaining weakness:** Canon, Workspace, provenance, ontology, and executability remain abstract vocabulary. The repository still asks a beginner to cross several documents, and no teenager or unrelated first-time reader has yet completed a timed test.

**Finding:** Structurally promising, empirically unvalidated.

### Expert

**What improved:** Specialists can move directly to canonical Questions, Challenges, model boundaries, Decisions, or the specification. Quests name expertise and evidence rather than asking for generic participation.

**Remaining weakness:** The repository has little external research evidence and no domain-specific reference Seed. Experts may correctly see a polished internal theory with insufficient comparative scholarship.

**Finding:** The navigation is ready for expert criticism; the evidence base is not mature.

### Designer

**What improved:** The experience has consistent page grammar, progressive disclosure, descriptive routes, monochrome-first presentation, limited badges, and text alternatives.

**Remaining weakness:** GitHub Markdown remains linear; the long README creates scroll depth; mobile behavior and assistive-technology use have not been observed directly. Duplicated explanations may drift.

**Finding:** Coherent within GitHub constraints, with maintenance and accessibility testing still required.

### Skeptic

**What improved:** The front door exposes unvalidated claims, current Challenges, model bias, and the possibility that the Seed should be rejected. Falsification has an obvious path.

**Remaining weakness:** The same system authored and evaluated the redesign. Time-to-understanding targets have not been tested by independent readers. The project may still be a documentation-heavy solution searching for a problem.

**Finding:** The repository now invites real attack, but self-review cannot validate the thesis.

## Result

The internal acceptance criteria for structure and discoverability are met. The hypothesis remains only partially tested because no independent timed reader study or semantic cold-start evaluation occurred.

## New evidence and next tests

1. Recruit at least one beginner, one domain expert, and one skeptical maintainer for timed entry tests.
2. Run X-0001 in two unfamiliar agent environments.
3. Build Project Lithos and one small unlike Seed to test whether these reader paths generalize.
4. Track every duplicated statement that drifts across README, Start Here, Bootstrap, and Canon.
5. Reassess whether eight issue forms reduce uncertainty or create choice overload.

## Failure conditions to watch

- readers cannot explain the Seed after three minutes;
- contributors cannot decide between Discussions, Issues, Challenges, and Quests;
- public polish is mistaken for protocol validation;
- maintenance burden causes routed documents to contradict Canon;
- the contribution experience attracts activity rather than useful correction.
