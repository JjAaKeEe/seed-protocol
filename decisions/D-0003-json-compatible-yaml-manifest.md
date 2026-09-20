# D-0003 — Use JSON-compatible YAML for the draft manifest

**Status:** accepted provisionally  
**Date:** 2026-09-20  
**Scope:** manifest serialization

## Context

The concept proposed `SEED.yaml`, but Python's standard library does not parse general YAML. Requiring a package manager and third-party parser would weaken the zero-dependency reference tool. Duplicating JSON and YAML manifests would create drift.

## Decision

For protocol 0.1-draft, `SEED.yaml` uses JSON syntax, which is valid YAML 1.2. The reference CLI parses it with the standard JSON library. The manifest declares `manifest_profile: json-compatible-yaml`.

## Alternatives considered

- require PyYAML;
- replace the manifest with `SEED.json`;
- replace it with TOML;
- maintain both a human YAML file and generated JSON file;
- implement a partial YAML parser.

## Consequences

- The tool remains dependency-free.
- Any JSON parser can read the manifest.
- The file is less pleasant for manual editing than conventional block YAML.
- Some users may find the `.yaml` extension surprising.

## Conditions for reconsideration

Revisit after template use shows whether manual-editing friction is material, or when a portable runtime dependency policy exists. Any change must include deterministic conversion and compatibility behavior.

