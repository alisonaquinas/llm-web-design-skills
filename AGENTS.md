# AGENTS.md — Guide for AI Agents Working in This Repo

## What This Repo Is

A collection of cross-compatible skills in `SKILL.md` format that help LLM agents reason about modern web frameworks, UI systems, static-site workflows, backend web platforms, and web build tooling.

## Repo Layout

```text
llm-web-design-skills/
├── .claude-plugin/plugin.json
├── linting/
├── validation/
├── skills/
│   └── <skill-name>/
│       ├── SKILL.md
│       ├── agents/
│       │   ├── openai.yaml
│       │   └── claude.yaml
│       ├── references/
│       ├── scripts/
│       └── assets/
├── docs/
├── AGENTS.md
├── INSTALL.md
├── LICENSE.md
└── README.md
```

## Invariants

- Every skill directory must contain `SKILL.md`.
- Every skill must contain `agents/openai.yaml` and `agents/claude.yaml`.
- SKILL.md frontmatter must contain only `name` and `description`.
- Any referenced file in the Intent Router must exist.

## Local quality gates

```bash
make lint
make test
make build
make verify
```

## Release Process

Before tagging a release, complete these steps in order:

1. **Update `.claude-plugin/plugin.json`** — set `"version"` to match the release tag (e.g., tag `v1.0.0` → `"version": "1.0.0"`). **This is enforced by CI.** The release workflow checks that the tag name equals the `version` field (with the leading `v` stripped). A mismatch causes an immediate failure: `ERROR: tag v1.0.0 does not match plugin.json version v0.1.0`.
2. **Update `CHANGELOG.md`** — rename `## [Unreleased]` to `## [<version>] - <YYYY-MM-DD>` and document all changes under `### Added`, `### Changed`, or `### Fixed`.
3. **Commit both files** with a `chore(release):` commit: `chore(release): bump to v<version>`.
4. **Create an annotated tag**: `git tag -a v<version> -m "Release v<version>"`.
5. **Push branch and tag**: `git push && git push origin v<version>`.

The release workflow (`.github/workflows/release.yml`) will then:

- Validate the tag matches `.claude-plugin/plugin.json`
- Run unit tests
- Run `make all` to build ZIP artifacts
- Create a GitHub Release with the ZIPs attached
- Trigger a marketplace rebuild on `alisonaquinas/llm-skills`
