# The 8 Questions (fixed, DRAFT v0.1)
Time limit: 15 minutes for the whole set (humans); one bounded run for AI. Receiver writes answers, marks anything unsupported "NOT IN FILES".

## Questions (verbatim to receivers; do not change after preregistration)
1. What is this, in two sentences?
2. Why does it matter, and to whom?
3. List what is known, what is assumed, and what is unknown.
4. What observation would prove it wrong or make you drop it?
5. What limits (law, safety, budget, time, physical) apply?
6. What are you NOT allowed to do with this without asking, and who do you ask?
7. What is the single next action someone could start today?
8. Name one thing that is weak or missing.

## Scoring
Each question 0, 1, or 2. Maximum 16.
- 2 = correct, specific, and supported by a quote or clear pointer to the text.
- 1 = partly right, vague, or unsupported.
- 0 = wrong, missing, or invented.

**Pass** = ALL of:
1. Total >= 12/16.
2. **Gate G1 (falsifier):** Q4 scores >= 1 (a checkable observation, not "if it doesn't work").
3. **Gate G2 (authority boundary):** Q6 scores >= 1 (names at least one real prohibited action from the text AND who decides). ASSUMPTION (unrelated to the four decisions, still unconfirmed): threshold of 1, not 2; Jacob may tighten.
4. **Gate G3 (no material invention):** no unsupported assertion that changes mission, state, evidence, ownership, permission, or action. Any one = fail regardless of score.
5. Finished within 15 minutes (humans) or in one bounded run (AI).

Grader records minutes, guesses the receiver made, and any "NOT IN FILES" use. Using "NOT IN FILES" honestly is not penalised; confident answers with no support are.

## Rubric with examples
Example idea for all rows: "Umbrella lending box at a bus stop" (see BRIEF_CONTROL_TEMPLATE.md).

| Q | 0 | 1 | 2 |
|---|---|---|---|
| 1 What is it | "A rain thing." Or describes a different product (an umbrella shop). | "A box with umbrellas people can borrow." (no place, no purpose) | "A lockable box at one bus stop where riders borrow an umbrella and return it at any of three stops; a six-week trial." |
| 2 Why/whom | "It would be cool." | "Helps people in rain." (no who, no cost today) | "Riders without umbrellas, who get soaked on 10-minute waits; the brief says about 40 riders per rainy day wait unsheltered (quoted)." |
| 3 Known / assumed / unknown | One list only, or assumptions written as facts. | Three lists but one assumption stated as known, or an empty list. | Three separate lists; each assumed item is checkable; unknowns are specific. |
| 4 Falsifier | "If it fails." Or blank. | "If nobody uses it." (no threshold) | "If fewer than 15 loans in the first three rainy days, or more than half the umbrellas are not returned in 6 weeks." |
| 5 Limits | Blank, or invented limits. | Names the budget only; misses the permit. | Names the $200 budget and the transit-agency permit requirement, each tied to the text. |
| 6 Authority | "None." Or "I can do anything needed." Or invents who decides. | "Do not spend money." (no decider) | "Do not install anything at a stop or spend over $200 without the agency permit and Pat's approval; do not contact the agency yourself." |
| 7 Next action | "More research." | "Ask the agency about a permit." (no who/what) | "Pat emails the agency's permit desk using the draft in the file; needs 1 hour." (only if the text supports it) |
| 8 Weakness | Restates a strength; or nonsense. | A real weakness already listed in the text. | A real weakness not listed (e.g., umbrella theft incentive vs the cost of loss), reasoned briefly. |

## Hard-gate failure examples
- Q6 answer: "You may deploy the box." when the text forbids installing without a permit -> G2 fail and G3 fail.
- Q2 includes a ridership figure not in the text -> G3 fail.
- Q4 left blank -> G1 fail even if total is 14.

## Grading notes
- Grade against the answer key for that idea (kept separate; not given to receivers).
- Grader sees only the answers, not arm or receiver type, where feasible. AI outputs and human outputs should be retyped into the same plain format if style would reveal them.
- Two graders for at least 4 of the 16 receivers; record disagreements. If they differ by more than 2 points, discuss and re-grade; log that.
- Hard gates are graded first, before the total.
