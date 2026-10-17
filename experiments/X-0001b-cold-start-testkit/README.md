# X-0001 Cold-Start Test Kit (DRAFT v0.1, 2026-10-17)
Status: DRAFT for Jacob. Nothing here has been run. No repo, PR, or Notion page was changed.

## Decisions (Jacob, Notion pre-read, 2026-10-17; see ../launch/JACOB_ANSWERS_2026-10-17.md)
- DECIDED D1: "Merge Now". PR #4 is to be merged BEFORE testing (reverses the old frozen-branch assumption). The test then runs against the merged main commit (record its SHA), not 055bfff. OPEN: Jacob has not authorized the merge action itself; confirm whether PR #4 merges unchanged.
- DECIDED D2: Spark is a protocol object, `SPARK.md` of 5 lines or fewer, as a working draft not frozen until 3 real promotions are observed.
- DECIDED D3: minimum Seed = smallest Seed that still passes a cold start; files, time, size are tie-breakers after passing.
- DECIDED D4: new templates default to UNDECIDED on purpose, written down; lawyer advice before investors/paid pilots. Test Seeds carry a line "license: UNDECIDED (by decision)". D-0004 supersede authorization: NOT confirmed (open). Note tension: merging PR #4 puts D-0008 (Apache-2.0 / CC BY 4.0) on main for the Golden Seed.

## Relation to the repo's existing X-0001
The repo's `experiments/X-0001-agent-cold-start.md` (status: ready, never run) tests agents only, uses 10 headings, 16/20, no time limit. This kit is a different test: 8 questions, 0-2 each, 15 minutes, pass 12/16 with hard gates, Seed vs one-page brief, humans and AI. The repo's own text says the rubric should change by a Decision, not quietly. So: **run this as "X-0001b" or file a Decision before calling it X-0001.** (Open decision.) Optional extra arm G: the repo's S-0000 scored with the repo's original 10-heading rubric, to keep that experiment honest.

## Purpose
Answer one question: does a Seed let a stranger understand and safely act on an idea better than a one-page brief of the same idea? If not, the format has not earned "bootable."

## Files
| File | Use |
|---|---|
| PREREGISTRATION.md | Freeze before anything runs |
| TWO_NEUTRAL_IDEAS.md | Draft test ideas; Jacob picks |
| BRIEF_CONTROL_TEMPLATE.md | Control arm format, with example |
| QUESTIONS.md | The 8 questions, rubric, gates |
| TESTER_INSTRUCTIONS.md | Hand to receivers (nothing else) |
| SCORESHEET.csv | 16 rows, one per receiver |

## Steps, time, who
| # | Step | Who | Time |
|---|---|---|---|
| 1 | Answer open decisions; pick 2 ideas; commit PREREGISTRATION.md (date it, do not edit after) | Jacob | 15 min |
| 2 | For each idea write the facts sheet (answer key source) | Jacob + Cord | 30 min/idea |
| 3 | Build Seed arm (from the minimal template, by hand) and brief arm from the same facts, same author, one page max each | Cord drafts, Jacob approves | 1 hr/idea |
| 4 | Write answer key per idea (what a correct answer to each question is) | Cord, Jacob checks; kept from receivers | 30 min/idea |
| 5 | Recruit 8 receivers: 4 humans who did not help build it (newcomers), plus 4 fresh AI contexts, at least 2 model families | Jacob recruits humans; Cord/Jacob launch AI | 1-3 days |
| 6 | Run: each receiver gets ONE arm of ONE idea (never both; they would contaminate). 15-minute limit | Receivers; a proctor for humans | 15 min each |
| 7 | Save raw outputs untouched | Proctor / Cord | - |
| 8 | Grade blind: strip arm labels and receiver type; grader is a person or AI that did not write the materials | Second person + a different AI | 15 min each |
| 9 | Fill SCORESHEET.csv, apply PREREGISTRATION pass rules, write result, including a failure | Cord | 1 hr |

Total: about 2 working hours of Jacob's time, 3-7 calendar days (mostly recruiting).

## Rules
- The author (Jacob/Cord) never coaches a receiver and never reads answers before grading is blind.
- Human consent: tell recipients that answers are kept and scored; no personal data collected beyond a first name and "newcomer: yes/no".
- AI receivers: fresh session, no memory, no browsing/tools beyond the files; record model, version, date, exact prompt.
- Do not publish results without Jacob's approval.
