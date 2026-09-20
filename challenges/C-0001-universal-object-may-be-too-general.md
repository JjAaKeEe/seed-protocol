# C-0001 — A universal Seed object may be too general to help

**Status:** open  
**Target:** central thesis, Q-0002  
**Severity:** foundational

## Claim

The protocol may mistake superficial similarity for a useful universal structure. An engineering research program, fictional universe, neighborhood initiative, and small software tool may share words such as “principles,” “questions,” and “history” while requiring incompatible operational semantics.

## Why this matters

If every Seed needs extensive customization, the protocol becomes a vague philosophy rather than an interoperable object. If it forces one schema on all domains, it may destroy precisely the nuance it intends to preserve.

## Evidence currently available

Only S-0000 has been implemented. Project Lithos influenced the design heavily. Cross-domain generality is untested.

## Proposed test

Apply the minimal profile to:

1. Project Lithos;
2. a small software tool;
3. a creative world or story;
4. a community practice.

Measure required exceptions, unused ceremony, information loss, and cold-start quality.

## Possible resolution

- preserve a very small universal core and define domain profiles;
- abandon universal structure in favor of a family resemblance;
- retain only a boot contract and let internal representation vary.

