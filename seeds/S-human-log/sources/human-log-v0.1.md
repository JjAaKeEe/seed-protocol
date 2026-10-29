# Human Log v0.1 — CoS evidence-graded Rolodex

**Intent (non-negotiable):** Thank, greet, help, support. Good-faith CoS memory extension — not surveillance. Purpose-bounded to Jacob's asks: thank-yous, BD, board/civic, pre-meeting prep, family logistics when requested.

**Adjacent to:** GitHub (versioned work) + Rolodex (who) + Seed Protocol (idea survival). Human Log is the **human-domain map**: entities (people, orgs) with chain-of-evidence → current-state-of-truth cards.

## Layers (mirror Seed Canon/Workspace/Evidence/History)

| Layer | What it holds |
|---|---|
| **Card (Canon)** | Current believed truth for an entity: preferred mail, phone, email, org ties, how we know them, next courtesy |
| **Claims (Workspace)** | Candidate facts not yet promoted |
| **Evidence** | Source links, registry pulls, as-of dates, CYA search log entries |
| **History** | Promotions, demotions, bounce/return mail, corrections |

## Evidence → truth (abstraction)

1. **Observe** — CRAWL search; append CYA log (query, URL, timestamp, summary). Never invent.
2. **Claim** — Extract candidate contact/identity with source + as-of.
3. **Correlate** — ≥2 identity anchors; namesake check; registered-agent ≠ mail; foundation PO Box > home street for mail purpose.
4. **Grade** — A registry/official · B own site · C corroborated secondary · D aggregator (Jacob OK) · X unresolved.
5. **Promote** — Grade A/B (or C with two sources) → Card field; keep Evidence linked. Demote on bounce/conflict.

## CoS ops cycle

```
Upcoming meet → Human Log pull/create stub → person-find fill gaps (purpose-scoped)
     → Meet (capture notes) → Thank-you / follow-up using graded mail
     → Update Card + Evidence → Idle until next trigger
```

Triggers: calendar invite with new person, Jacob asks "find address", post-call voice dump, HubSpot/form lead that needs a human card.

## Entity types

- Person, Organization, Foundation/Nonprofit, Role-at-org (edge), Household (careful — family logistics only on ask)

## Connectors (map)

| Source | Role today | Gap |
|---|---|---|
| Personal OneDrive OSINT pack | Method training | Done ingest |
| Notion | Joint command notes | Need Human Log DB or page pattern |
| Gmail/Outlook | Meeting/thank-you threads | Parse for contact crumbs |
| Calendar | Meet triggers | Pre-brief hook |
| HubSpot | Lead cards | BD contacts ≠ personal mail |
| State SOS / IRS TEOS / charity | Grade A mail | Need registry-ladder helper |
| Phone contacts / Vault | Known good | Prefer over hunt when present |
| Aggregators | Leads only | Never promote alone |

## Software seeds (build now — Jacob greenlit)

1. **confidence-grader** — pure function + CLI
2. **cya-log** — append-only JSONL per case
3. **entity-card schema** — JSON Schema for Card/Claim/Evidence
4. **registry-ladder** checklist CLI
5. Seed Protocol plant: this document as Seed S-???? Human Log

## Non-goals

No pretexting, no unauthorized access, no FCRA/GLBA/DPPA data, no SSNs/minors, no group-chat dump of private home/phone.
