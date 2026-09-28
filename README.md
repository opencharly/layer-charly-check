# charly-check

The `charly-check` family — the check orchestration and probe-verb skills.

The `charly-check` candy is a **concept candy**: it ships no install content and
owns the `check` family of `skill:` entities that document charly's evaluation
surface — `check` (orchestration, plans, disposable beds, R10) and the
out-of-process probe verbs `adb`, `android`, `appium`, `cdp`, `dbus`, `libvirt`,
`record`, `spice`, `vnc`, `jetkvm`, `console-automation`, `cua`, and the
`check-sway-browser-vnc` bed. `candy/plugin-marketplace` regenerates the
standalone [opencharly/marketplace](https://github.com/opencharly/marketplace)
corpus from these entities, so the skills are authored here and projected there.

## What it provides

| Property | Value |
|---|---|
| Layer / candy | `charly-check` (concept candy) |
| Install content | none — a `true` no-op `plan:` |
| Owns | 14 `skill:` entities in the `check` family |
| Projected to | `marketplace/check/skills/` |
| Service / port | none |

## How to use it

This repo is consumed as a **skill source**, not as an image layer. Edit the
`skill:` entities in `charly.yml`; the marketplace regeneration projects them
into `/charly-check:*` pages. To reference the repo directly:

```yaml
my-box:
  candy:
    base: fedora
    candy:
      - '@github.com/opencharly/layer-charly-check:v2026.271.1956'
```

## Layout

- `charly.yml` — the `charly-check:` concept candy entity plus 14 `skill:`
  entities (`check`, `adb`, `android`, `appium`, `cdp`, `check-sway-browser-vnc`,
  `dbus`, `libvirt`, `record`, `spice`, `vnc`, `jetkvm`, `console-automation`,
  `cua`).
- `.github/workflows/tag-on-merge.yml` — CalVer tag + `CHANGELOG/` on merge.
- `README.md` — this user overview.

## Related

- Owning skill: `/charly-check:check`
- Authoring reference: `/charly-image:layer`
- [`opencharly/marketplace`](https://github.com/opencharly/marketplace) — the projected corpus
- [`opencharly/charly`](https://github.com/opencharly/charly) — the charly CLI and image builder
- [`opencharly/opencharly`](https://github.com/opencharly/opencharly) — the umbrella
