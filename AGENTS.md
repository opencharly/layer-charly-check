# AGENTS.md — layer-charly-check

Standalone candy repo for the `charly-check` concept candy — it ships no install
content and owns the `check` family of `skill:` entities that document charly's
evaluation surface and probe verbs. The entities live in `charly.yml` at the
repo root and each skill's BODY lives beside it, in `.agents/skills/<name>/SKILL.md`;
`candy/plugin-marketplace` regenerates the standalone opencharly/marketplace
corpus from them.

Canonical files:

- `charly.yml` — the `charly-check:` concept candy entity plus 14 `skill:` routing
  nodes (`check`, `adb`, `android`, `appium`, `cdp`, `check-sway-browser-vnc`,
  `dbus`, `libvirt`, `record`, `spice`, `vnc`, `jetkvm`, `console-automation`,
  `cua`), each carrying `name`/`family`/`owner`/`triggers` and no body.
- `.agents/skills/<name>/SKILL.md` — the 14 skill BODIES, one directory per node's
  `name:`, plus `references/*.md` where a body splits (the `check` skill's four).
  The files are the source of record for the prose.
- `.github/workflows/tag-on-merge.yml` — CalVer tag + `CHANGELOG/` on merge.
- `README.md` — user overview only; never agent guidance.

## Load these skills first (R0)

- `/charly-check:check` — the owning skill for this repo's family (orchestration,
  plans, disposable beds, R10). Load before editing the concept candy or any of
  its `skill:` entities.
- `/charly-image:layer` — the candy authoring reference (`charly.yml` schema,
  `plan:` step verbs incl. `check:`, package sections, service declarations).
  Load before editing any entity field or plan step.

## Build / validate / test

- `charly box validate` at the repo root — the structural check: the manifest
  must parse and validate at the installed charly.
- The merge gate is the **org-wide** `charly/pr-validator` (required check
  `validate / validate`, defined in `opencharly/.github`); this repo has no
  per-repo candy gate.
- The candy is documentation-only: its `plan:` is a `true` no-op plus a `true`
  `check:` that the skill entities are present and generated into the
  marketplace. There is no live bed.

## Modify this repo

- Edit a skill's `SKILL.md` under `.agents/skills/<name>/` for the prose, or its
  node in `charly.yml` for the routing — never the generated `SKILL.md` in the
  marketplace corpus; a corpus regeneration (`charly marketplace generate`)
  projects both.
- When a check verb's behaviour or a bed's roster changes, update the matching
  `skill:` entity in the same change so the corpus does not drift.
- Keep the concept candy's `plan:` no-op; it exists only to carry the entities.

## Landing

- PR-only. Every change lands through a pull request; the org-required
  `charly/pr-validator` validates the diff and body and arms native auto-merge
  on PASS. Direct pushes to `main` are blocked.
- History lives in `CHANGELOG/` (written by `tag-on-merge` at merge time); the
  PR body IS the changelog.
- The authoritative rulebook is the umbrella `AGENTS.md` in
  `opencharly/opencharly` and `charly/AGENTS.md` in the charly repo. Do not
  restate its rules here.
