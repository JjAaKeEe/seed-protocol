# Preregistration: X-0001 Cold-Start (DRAFT, not yet frozen)
Write once. Once Jacob approves, date it and commit a copy; any later change must be logged below as an amendment, with the reason. Written before any receiver sees any material.
Frozen on: ______ (not frozen)  Approved by: ______

## Decisions carried (Jacob, 2026-10-17; verbatim answers were cited from ../launch/JACOB_ANSWERS_2026-10-17.md, which is not in this repository)
Merge PR #4 first ("Merge Now"; test version = merged main SHA, recorded at freeze); Spark = SPARK.md of 5 lines or fewer, working draft; minimum Seed = smallest that passes a cold start; templates default UNDECIDED by decision (license line in test Seeds says so). OPEN: merge authorization, D-0004 supersede.

## Hypothesis
H1: A stranger given a Seed for an unfamiliar idea can answer the 8 questions better than a stranger given a one-page brief of the same facts: higher mean score, and more receivers passing all gates.
H0: There is no meaningful difference (or the brief does better).

## Design
- Ideas: 2, unlike each other (see TWO_NEUTRAL_IDEAS.md), fictional fixtures.
- Arms: Seed (S) vs one-page brief (B).
- Receiver type: human newcomer (H) vs fresh AI context (AI).
- Cells: 2 ideas x 2 arms x 2 receiver types = 8 cells, 2 receivers per cell = 16 receivers. Each receiver gets one arm of one idea only.
- AI contexts: at least 2 model families; fresh session, no tools.
- Time: 15 minutes (humans), one bounded run (AI).
- Instrument: QUESTIONS.md, unchanged. Answer key written and sealed before the run.
- Grading: blind to arm and receiver type where feasible; grader did not write the materials; second grader on at least 4 receivers.
- Optional arm G (repo S-0000 with the repo's 10-heading, 16/20 rubric) run separately; not part of the pass rules below.

## Pass definition (per receiver)
Total >= 12/16, Q4 >= 1, Q6 >= 1, no material invention, within time. (See QUESTIONS.md.)

## Success criteria for the Seed (all must hold)
1. Seed arm: at least 6 of 8 receivers pass.
2. Seed arm mean score exceeds brief arm mean by at least 2.0 points (of 16).
3. Seed arm passes at least 2 more receivers than the brief arm (e.g., 6 vs 4).
4. Seed arm passes in both ideas (at least 2 of 4 receivers per idea) AND in both receiver types (at least 2 of 4 for H and for AI).
5. No Seed-arm receiver fails G2 (authority) with an action that would have been unsafe or unauthorized.

If all five hold: label this version "cold-start passed (n=16)". This supports "viable", not "proven"; n is small.

## What would falsify / count against the hypothesis
- Seed arm passes fewer than 6 of 8.
- Seed mean is less than 2.0 points above the brief mean, or at or below it.
- Brief arm passes as many as or more than the Seed arm. Then the Seed adds structure without adding comprehension; the conclusion is "the one-page brief is enough" for these cases.
- Seed passes with AI but not humans (or reverse): then it works for one reader type only; narrow the claim.
- Seed works for one idea only: not demonstrated as general.
- Hard-gate failures concentrated in Q4 or Q6 in the Seed arm: the template fails to carry falsifiers or authority.
Report any of these plainly. A failed test is a result, not an error.

## Known limits, stated now
- n=16; one reader per cell is an anecdote; treat results as pilot.
- Fictional fixtures reduce training-data contamination but may be less realistic.
- The 12/16, 15 min, equal weights and the question wording are hypotheses, not validated findings.
- Graders may infer arm from style; mitigated by retyping, not eliminated.
- The Seed arm writer is also the repo author's agent; build the Seeds from the template with no extra polishing beyond the facts sheet.
- AI receivers vary run to run; one run per cell is noise-prone. If budget permits, repeat AI cells 3 times and use the median.

## What gets recorded
Raw outputs, model/environment, prompt, times, file versions, graders' scores and notes, disagreements, all deviations.

## Amendments
- 2026-10-17: The kit was added to the repository before any receiver saw it. D-0004 was marked superseded by D-0008 and D-0009 in that landing (see those decisions). This preregistration is still not frozen. The experiment has not been run. No merged SHA is recorded here because the test has not been frozen.
