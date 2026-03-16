---
name: angular
description: >
  review, design, scaffold, refactor, and troubleshoot angular applications and libraries. use when the user asks for angular architecture, components, signals, rxjs usage, dependency injection, routing, forms, testing, or migration guidance.
---

# Angular

Use this skill to keep Angular work grounded in maintainable architecture, predictable delivery, and framework-appropriate conventions.

## Intent Router

| Need | Load |
| --- | --- |
| core conventions, structure, review priorities, and common red flags for Angular | `references/best-practices.md` |
| setup, migration, testing, build, delivery, and day-two workflow guidance for Angular | `references/workflows.md` |

## Quick Start

1. Confirm Angular version and workspace toolchain, standalone APIs versus NgModules, SSR, SSG, or client-only rendering, and signals, RxJS, or store posture.
2. Identify whether the task is greenfield scaffolding, incremental refactoring, troubleshooting, migration planning, or code review.
3. Apply the defaults in `references/best-practices.md` before proposing custom architecture.
4. Prefer the smallest change set that improves clarity, safety, operability, and long-term maintainability.

## Workflow

- identify feature ownership before editing local files
- separate framework defaults from UI-kit or backend-specific choices
- protect routes, forms, and template behavior during refactors
- verify build and tests after structural changes

## Typical Focus Areas

- Angular version and workspace toolchain
- standalone APIs versus NgModules
- SSR, SSG, or client-only rendering
- signals, RxJS, or store posture

## Outputs to Prefer

- summarize version, rendering, and state constraints first
- group findings by feature boundary, state, routing, forms, and tests
- prefer small refactors over framework-wide rewrites

## First Response Pattern

- restate Angular version, rendering mode, and state posture before suggesting changes
- anchor the plan at the owning feature, route, or form boundary instead of proposing app-wide rewrites
- name the verification loop up front: `ng build`, `ng test`, and a smoke test of the affected route or form

## Common Requests

```text
Review this Angular feature for standalone structure, signals versus RxJS usage, routing, and test gaps.
```

```text
Refactor this Angular form flow to be more maintainable without changing user-visible behavior.
```

## Safety Notes

- preserve externally visible behavior unless the user explicitly requests a redesign or a breaking change
- avoid style-only churn when the current repository already has working conventions and automation
