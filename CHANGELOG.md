# Changelog

## [Unreleased]

### Added (Codex marketplace)

- Added `.codex-plugin/plugin.json` so the web design skills bundle can be published through a Codex plugin marketplace.
- Added `scripts/validate_plugin_manifests.py` and `make codex-bundle` to validate Codex/Claude manifest alignment and build `web-design-skills-codex-plugin.zip`.

## [1.1.5] - 2026-03-31

### Fixed (1.1.5)

- Replaced broken `SessionStart` prompt hook in `hooks/hooks.json` with a working `command`-type hook that invokes the session-start script, eliminating "ToolUseContext is required for prompt hooks" startup errors.

## [1.1.4] - 2026-03-22

### Fixed (1.1.4)

- Removed broken `SessionStart` prompt hook from `hooks/hooks.json`. The `type: "prompt"` hook requires a `ToolUseContext` that does not exist at session start, causing "ToolUseContext is required for prompt hooks" errors on every startup.

## [1.1.3] - 2026-03-16

### Added (1.1.3)

- Added repository-wide skill agent manifest (agents/web-maintainer.md), command entries, and hooks/hooks.json for consistent skill routing across Claude and Codex clients.
- Extended AGENTS.md with command + agent template section for focused web-design skill loops.

### Changed (1.1.3)

- Hardened scripts/verify_built_zips.py with REQUIRED_FILES invariant checks.

## [1.1.2] - 2026-03-18

### Fixed

- Enforced repository-rooted ZIP layout checks so built skill packages include required files under `llm-web-design-skills/skills/<skill>/...` and fail early when this contract is broken.

## [1.1.1] - 2026-03-18

### Added (release automation)

- Added repository-wide skill agent and command scaffolding for all skills, including per-skill `agents/` manifests and `commands/` entries, so skill invocations can be routed consistently by both Claude and Codex clients.
- Added `hooks/hooks.json` with preconfigured hooks for agent selection and command execution orchestration.

## [1.1.0] - 2026-03-16

### Added (1.1.0)

- `Makefile`: added `bundle` target that packages all built `*-skill.zip` files into a single `web-design-skills-plugin.zip` for one-click offline installation; `PLUGIN_NAME := web-design-skills` variable drives the output filename

### Changed (1.1.0)

- `Makefile`: extended `.PHONY` to include `bundle`; updated `help` text to document the new target
- `.github/workflows/release.yml`: upgraded from minimal stub to full plugin release pipeline — adds version gate, changelog extraction, `softprops/action-gh-release` upload of `built/*.zip` (including `web-design-skills-plugin.zip`), `changelog` extraction, and marketplace dispatch trigger; added "Build plugin bundle ZIP" step (`make bundle`)

## [1.0.0] - 2026-03-16

- Initial release of `llm-web-design-skills`.
- Added 16 cross-compatible web framework and web design skills:
  - **Frontend frameworks**: `angular`, `nextjs`, `react`, `svelte`, `vue`
  - **Styling and UI systems**: `material-design`, `scss`, `tailwind`
  - **Build and tooling**: `vite`
  - **Backend frameworks**: `django`, `nodejs`, `express-js`, `asp-net`, `spring-boot`, `laravel`
  - **Static sites and content**: `hugo`
- Each skill ships with Claude and OpenAI agent definitions, best-practices reference, and workflow guide.
