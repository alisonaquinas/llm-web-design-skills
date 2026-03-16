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
