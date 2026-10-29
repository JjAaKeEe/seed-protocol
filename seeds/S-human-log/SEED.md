# Human Log

Canon for this Seed is the accepted working account below. It coordinates the idea. It is open to challenge and is not a claim that the practice has been shown to work.

## Origin

Jacob Nelson (chief of staff) and Cord, 2026-10-29. The stated context is OSINT Academy / US-SOCOM Foundations training applied to chief-of-staff operations. Human Log is adjacent to Rolodex (who), GitHub (versioned work), and Seed Protocol (idea survival).

The planting source is the Human Log v0.1 design note, copied verbatim at `sources/human-log-v0.1.md`. This file distills that note into Seed form. Where they disagree, treat the disagreement as unresolved and record it; do not silently pick a newer gloss.

## Problem or possibility

Human memory and agent memory are insufficient for thanking, greeting, and helping people across meetings. Contact truth is scattered and ungraded.

The intent is a good-faith chief-of-staff memory extension: thank, greet, help, and support. Purpose stays inside Jacob's asks: thank-yous, business development, board and civic work, pre-meeting preparation, and family logistics when requested.

## Core thesis

Map the human domain as evidence-graded entity cards for persons and organizations. A fact reaches a card only along this chain:

1. **Observe.** Search by CRAWL. Append a CYA log entry with query, URL, timestamp, and summary. Leave unknown fields unknown.
2. **Claim.** Extract a candidate contact or identity fact with its source and an as-of date.
3. **Correlate.** Require at least two identity anchors. Check namesakes. A registered-agent address is not a mail destination. For a courtesy-mail purpose, an entity's official mail or PO Box outranks a home street; the design note states the same preference as foundation PO Box over home street.
4. **Grade.** A is registry or official. B is the entity's own site. C is a corroborated secondary source. D is an aggregator and needs Jacob's OK. X is unresolved.
5. **Promote.** Grade A or B, or grade C with two sources, may fill a Card field. Keep the Evidence linked. Demote the field on bounce or conflict. A grade D aggregator is a lead and is never promoted alone.

## Principles

Principles that change a choice live in `context/principles.md`. The short list:

- Good faith only: thank, greet, help, support, inside the asks named above.
- Public lawful sources only.
- Contact data is recorded from a source, or it stays blank.
- Registered-agent addresses stay off courtesy mail.
- Entity official mail or a PO Box is the courtesy-mail target ahead of a home street.
- Private home and phone stay in one-to-one use with the owner, and stay out of group channels.
- FCRA, GLBA, and DPPA data, SSNs, and minors are out of scope.
- Grades govern promotion. Ignoring a grade, or promoting an aggregator alone, breaks the Seed.

## Concept model

Human Log mirrors Seed layers with entity records:

| Layer | What it holds |
|---|---|
| **Card (Canon)** | Current believed truth for one entity: preferred mail, phone, email, org ties, how we know them, next courtesy |
| **Claims (Workspace)** | Candidate facts not yet promoted |
| **Evidence** | Source links, registry pulls, as-of dates, CYA search-log entries |
| **History** | Promotions, demotions, bounce or return mail, corrections |

Entity types: Person, Organization, Foundation/Nonprofit, Role-at-org (an edge), and Household. Household is for family logistics only when that ask is made.

Chief-of-staff cycle, as stated in the design note:

```
Upcoming meet → Human Log pull/create stub → person-find fill gaps (purpose-scoped)
     → Meet (capture notes) → Thank-you / follow-up using graded mail
     → Update Card + Evidence → Idle until next trigger
```

In prose: before a meeting, pull or create a stub; fill gaps with a purpose-scoped person-find; capture notes at the meeting; send the thank-you or follow-up to graded mail; update the card and its evidence; then leave the record idle until the next trigger.

Triggers named in the design note: a calendar invite with a new person, Jacob asking to find an address, a post-call voice dump, and a HubSpot or form lead that needs a human card.

Connectors, in the state the design note gives them. "Role today" is the note's statement, not a check performed in this planting:

| Source | Role today | Gap |
|---|---|---|
| Personal OneDrive OSINT pack | Method training | Done ingest |
| Notion | Joint command notes | Need a Human Log database or page pattern |
| Gmail/Outlook | Meeting and thank-you threads | Parse for contact crumbs |
| Calendar | Meet triggers | Pre-brief hook |
| HubSpot | Lead cards | Business-development contacts are not personal mail |
| State SOS / IRS TEOS / charity registries | Grade A mail | Need a registry-ladder helper |
| Phone contacts / Vault | Known good | Prefer these over a hunt when they are present |
| Aggregators | Leads only | Never promote alone |

## Existing work and precedents

The design note places Human Log beside three existing practices: GitHub for versioned work, a Rolodex for who someone is, and Seed Protocol for keeping an idea recoverable. This Seed adopts the minimal Seed file set so the idea can sit still without its chat.

The same note says Jacob greenlit four software efforts to build separately, plus this planting:

1. **confidence-grader** — a pure function and a command-line interface.
2. **cya-log** — an append-only JSONL log per case.
3. **entity-card schema** — JSON Schema for Card, Claim, and Evidence.
4. **registry-ladder** — a checklist command-line interface.
5. This Seed, planted from that note.

None of those four tools are in this directory. Opening them is a later repository, not a silent addition here.

## Assumptions and evidence

**Recorded in this Seed.** The v0.1 design note, the planting date, and the attribution to Jacob Nelson (CoS) and Cord. Validation of this directory checks file structure only.

**Stated as the problem, not measured here.** Human memory and agent memory fail the courtesy tasks above, and contact truth is scattered and ungraded.

**Operating rules taken from the note.** The grade scale, the two-anchor correlation rule, the promotion rule, the registered-agent rule, and the mail-address preference. They are accepted for coordination. They have no trial log, bounce log, or card corpus in this Seed.

**Stated connector status.** The table above, including "done ingest" for the personal OneDrive OSINT pack. This Seed does not contain that pack.

**Not built.** The Notion Human Log database, the calendar pre-brief, mail-crumb parsing, confidence-grader, cya-log, the entity-card schema, and registry-ladder.

## Failure conditions

The idea has failed, or must stop, if any of these become true:

- It becomes surveillance.
- Grades are ignored.
- An aggregator is promoted alone.
- It is used for harassment.
- The structure kills the spontaneity of a thank-you.

The design note also excludes pretexting, unauthorized access, FCRA/GLBA/DPPA data, SSNs, minors, and dumping a private home or phone into a group chat. Crossing those lines is a failure of this Seed, not a feature.

## Open directions

Another participant can explore these without treating them as Canon:

- A Notion Human Log database, or a page pattern, for the living cards.
- Connectors, including a calendar pre-brief and mail crumbs from meeting and thank-you threads.
- confidence-grader and cya-log as software in a separate repository, along with the entity-card schema and the registry-ladder checklist.

Questions for that work are in `context/questions.md`.

## If you want to run with this

Read this file, `context/principles.md`, and `context/model-boundary.md` before adding a card. The grade chain and the good-faith boundary are the parts that are stable enough to apply. Whether cards actually improve thank-yous, and whether the structure stays light enough to use, is untested.

Nothing in the software list has been built in this Seed. The next useful action is in `context/status.md`: sketch Card, Claim, and Evidence fields in Workspace and leave them unpromoted.

Reading this Seed and researching public lawful sources are autonomous. Sending mail, greeting someone, or otherwise contacting a person requires explicit approval. Do not invent an address, email, or phone number to fill a gap.
