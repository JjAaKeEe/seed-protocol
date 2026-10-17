# D-0009 — Template licenses UNDECIDED by design; minimum Seed; Spark

**Status:** accepted (owner decision, 2026-10-17)

## Decisions
1. **Template licenses.** Seeds created from `templates/` default every license field to `UNDECIDED`, deliberately and in writing. Any Golden Seed license choice does not transfer. Obtain legal advice before investors or paid pilots.
2. **Minimum Seed.** The minimum Seed is the smallest Seed that still passes a cold start (X-0001b). File count, time to plant, and size are tie-breakers only. Until X-0001b has run, no minimum is established; the 8-item spec list and 9-file template are working assumptions.
3. **Spark.** A Spark is a protocol object: `SPARK.md`, 5 lines or fewer, a working draft (see `spec/SPARK-draft.md`), not frozen until three real Spark-to-Seed promotions are observed.
4. **Quests are non-scored** until C-0003 has evidence (see `ROADMAP.md`).

## Note
When this decision was written, the Golden Seed license posture was still pending an owner re-decision, and D-0004 supersession plus a root `LICENSE` file were deferred.

That deferral ended the same day in D-0010. Spec text, the manifest format, and `tools/seed.py` are Apache-2.0. Explanatory docs stay CC BY 4.0. Decision 1 above is unchanged: template files carry no license-grant strings, and a new Seed's license fields stay `UNDECIDED`. D-0004 is superseded by D-0008 and D-0009. Lawyer review is still open. X-0001b has not been run, so no minimum Seed is established.
