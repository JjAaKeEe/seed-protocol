# Contributing to Seed Protocol

You may contribute once without joining anything. Questions, corrections, evidence, prior art, experiments, design criticism, and proof that the protocol is wrong are all welcome.

## Choose a route

### First-time contributor

Read [`START-HERE.md`](START-HERE.md), then choose a D1 or D2 task from [Find a Quest](docs/FIND-A-QUEST.md). The smallest valuable contribution may be one confusing sentence, a missing example, or a relevant project this repository failed to acknowledge.

No command line is required. Use a GitHub Discussion or the **First contribution** issue form.

The [community map](docs/COMMUNITY.md) links the welcome, attack, and contribution-matching Discussions.

### Domain expert

You do not need to learn the entire protocol. Find a Question matching your expertise, state the limits of your claim, and provide a source, field observation, counterexample, or decision pattern. It is acceptable to contribute once and leave.

### Researcher

Connect evidence to an existing Question, Challenge, or Experiment. Prefer primary sources, reproducible methods, explicit uncertainty, and observations that could change the project’s confidence—not reference volume alone.

### Designer or editor

Test the 30-second, 3-minute, 10-minute, and 20-minute reader journeys. Report navigation loops, jargon, inaccessible diagrams, false confidence, redundant layers, or places where the system makes a simple action feel administrative.

### Agent or tool builder

Run the cold-start experiment, test a different agent environment, examine context routing, or improve validation without making the protocol vendor-dependent. Record the exact environment, prompt, output, authority mistakes, and handoff quality.

### Skeptic or red teamer

Read [Attack the Seed](docs/ATTACK-THE-SEED.md). A serious Challenge that invalidates a foundational assumption is more valuable than a supportive rewrite. Attack claims and systems, not contributors.

## Find work

- [Current Quests and Boss Problems](docs/FIND-A-QUEST.md)
- [Canonical open Questions](context/questions.md)
- [Current Challenge index](challenges/README.md)
- [Designed Experiments](experiments/)
- [Current status and handoff](context/status.md)

If nothing fits, open an Idea or Question. Do not invent work merely to produce activity.

## Choose the lightest contribution surface

| Surface | Use it for |
|---|---|
| **Discussion** | Early questions, incomplete ideas, offers of expertise, or conversation |
| **Issue** | A bounded Question, Challenge, evidence item, experiment, documentation defect, or proposed task |
| **Pull request** | A concrete reviewable change to the repository |
| **Fork** | A fundamental direction that should evolve independently |

### GitHub words in plain language

- An **issue** is a tracked request or problem.
- A **Discussion** is a conversation that does not yet need a repository change.
- A **branch** is an isolated line of edits.
- A **commit** is a recorded group of changes.
- A **pull request** asks maintainers to review and merge a branch.
- A **fork** is your own copy that can diverge from this project.

## Before changing files

1. Read [`SEED.yaml`](SEED.yaml) and [`BOOTSTRAP.md`](BOOTSTRAP.md).
2. Check [`context/status.md`](context/status.md) and the relevant Questions, Decisions, and Challenges.
3. Keep Canon, Workspace, Evidence, and History distinct.
4. Preserve uncertainty and provenance.
5. Do not infer permission for outreach, spending, fabrication, or physical action.

## When a record is warranted

- Use a **Decision** when a meaningful accepted choice needs rationale, alternatives, consequences, and reversal conditions.
- Use a **Challenge** when an objection deserves to survive the conversation that raised it.
- Use an **Experiment** when a method can reduce uncertainty and produce inspectable observations.
- Use an ordinary issue or discussion when the question is still forming.

Do not create protocol objects as ceremony.

## Pull-request expectations

- Explain the problem before the solution.
- Identify whether the change affects Canon, specification, tooling, public experience, or only Workspace.
- Link the relevant Question, Decision, Challenge, or Experiment when one exists.
- Update navigation, status, changelog, provenance, or tests when the change makes them stale.
- Include text alternatives for Mermaid diagrams.
- Keep claims proportional to evidence.
- Avoid unrelated cleanup.

For code changes, run:

```sh
python3 tools/seed.py validate .
python3 -m unittest discover -s tests -v
```

For documentation changes, also verify relative links, headings, Mermaid rendering, and the human/agent entry routes.

## Conduct

Be direct, charitable, and evidence-oriented. Critique ideas vigorously without attacking people. Acknowledge uncertainty. Preserve contributor attribution. Do not expose private source material or personal information.

## Rights and attribution

By contributing, you agree that your contribution may be distributed under the repository’s applicable licenses: Apache-2.0 for software and CC BY 4.0 for prose, documentation, diagrams, data, and media unless explicitly stated otherwise. See [`LICENSE.md`](LICENSE.md).

## What success looks like

A contribution is successful when it reduces uncertainty, transfers knowledge, prevents repeated failure, improves entry for the next participant, or reveals that the Seed should change or die. Activity by itself is not success.
