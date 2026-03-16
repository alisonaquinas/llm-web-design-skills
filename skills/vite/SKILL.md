---
name: vite
description: >
  review, design, scaffold, refactor, and troubleshoot vite based web projects and toolchains. use when the user asks for vite app structure, dev server behavior, bundling, plugins, env variables, aliasing, asset handling, test integration, or migration guidance.
---

# Vite

Use this skill to keep Vite work grounded in maintainable architecture, predictable delivery, and framework-appropriate conventions.

## Intent Router

| Need | Load |
| --- | --- |
| core conventions, structure, review priorities, and common red flags for Vite | `references/best-practices.md` |
| setup, migration, testing, build, delivery, and day-two workflow guidance for Vite | `references/workflows.md` |

## Quick Start

1. Confirm Vite version and framework plugin stack, dev-server versus build-time problem scope, artifact type: app, library, or docs site, and deployment target and env strategy.
2. Identify whether the task is greenfield scaffolding, incremental refactoring, troubleshooting, migration planning, or code review.
3. Apply the defaults in `references/best-practices.md` before proposing custom architecture.
4. Prefer the smallest change set that improves clarity, safety, operability, and long-term maintainability.

## Workflow

- identify whether the problem is in dev, build, preview, or tests
- keep alias and env naming aligned across tools
- separate functional correctness from performance tuning
- verify preview and production-like behavior after config changes

## Typical Focus Areas

- Vite version and framework plugin stack
- dev-server versus build-time problem scope
- artifact type: app, library, or docs site
- deployment target and env strategy

## Outputs to Prefer

- summarize framework host, artifact type, and deployment constraints first
- group findings by config, plugins, env handling, assets, and preview behavior
- prefer solving the correct layer: dev server, build, test, or deploy

## First Response Pattern

- restate Vite version, plugin stack, and whether the problem is in dev, build, preview, or tests before suggesting changes
- anchor the plan at the affected config seam such as aliases, plugins, env, or asset handling
- name the verification loop up front: `npm run dev`, `npm run build`, and either `npm run preview` or `npm run test` for the changed path

## Common Requests

```text
Review this Vite config for plugin order, aliasing, asset handling, preview behavior, and `import.meta.env` safety in a React or Vue app where `npm run dev` works but `npm run build` or `npm run preview` drifts from local behavior.
```

```text
Help migrate this frontend project from webpack or CRA to Vite with minimal churn while preserving plugin behavior, Vitest coverage, path aliases, and preview parity for the current deployment target.
```

## Safety Notes

- preserve externally visible behavior unless the user explicitly requests a redesign or a breaking change
- avoid style-only churn when the current repository already has working conventions and automation
