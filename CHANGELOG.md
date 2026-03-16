# Changelog

## [1.1.0] - 2026-03-16

### Added

- `Makefile`: added `bundle` target that packages all built `*-skill.zip` files into a single `web-design-skills-plugin.zip` for one-click offline installation; `PLUGIN_NAME := web-design-skills` variable drives the output filename

### Changed

- `Makefile`: extended `.PHONY` to include `bundle`; updated `help` text to document the new target
- `.github/workflows/release.yml`: upgraded from minimal stub to full plugin release pipeline — adds version gate, changelog extraction, `softprops/action-gh-release` upload of `built/*.zip` (including `web-design-skills-plugin.zip`), and marketplace dispatch trigger; added "Build plugin bundle ZIP" step (`make bundle`)

## [1.0.0] - 2026-03-16

- Initial release of `llm-web-design-skills`.
- Added 16 cross-compatible web framework and web design skills:
  - **Frontend frameworks**: `angular`, `nextjs`, `react`, `svelte`, `vue`
  - **Styling and UI systems**: `material-design`, `scss`, `tailwind`
  - **Build and tooling**: `vite`
  - **Backend frameworks**: `django`, `nodejs`, `express-js`, `asp-net`, `spring-boot`, `laravel`
  - **Static sites and content**: `hugo`
- Each skill ships with Claude and OpenAI agent definitions, best-practices reference, and workflow guide.
