# X-0002 — Cross-domain fit

**Status:** designed  
**Questions:** Q-0001, Q-0002, Q-0060, Q-0061

## Hypothesis

The minimal Seed core can represent at least three substantially different ideas without material loss or excessive ceremony.

## Cases

1. Project Lithos — complex interdisciplinary research and design.
2. A small software idea — bounded and executable.
3. A creative Seed — world, story, artwork, or game without a conventional falsifiable thesis.

## Measures

- number of required core fields that are useful;
- number of required fields left artificial or empty;
- domain-specific extensions needed;
- time to create the first useful Seed;
- cold-start accuracy for human and agent readers;
- concepts lost or distorted;
- duplicate maintenance burden;
- author willingness to use the structure again.

## Decision rule

If more than a small universal core is consistently artificial across domains, split the specification into:

- a universal boot and identity core; and
- optional domain profiles.

