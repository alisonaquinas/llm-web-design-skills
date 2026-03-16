---
name: vue
description: >
  review, design, scaffold, refactor, and troubleshoot vue applications and component libraries. use when the user asks for vue component design, composition api patterns, state management, routing, forms, testing, vite integration, or migration guidance.
---

# Vue

Use this skill to keep Vue work grounded in maintainable architecture, predictable delivery, and framework-appropriate conventions.

## Intent Router

| Need | Load |
| --- | --- |
| core conventions, structure, review priorities, and common red flags for Vue | `references/best-practices.md` |
| setup, migration, testing, build, delivery, and day-two workflow guidance for Vue | `references/workflows.md` |

## Quick Start

1. Confirm Vue version and host environment, Composition API, Options API, or mixed posture, router and store strategy, and app, library, or admin-surface scope.
2. Identify whether the task is greenfield scaffolding, incremental refactoring, troubleshooting, migration planning, or code review.
3. Apply the defaults in `references/best-practices.md` before proposing custom architecture.
4. Prefer the smallest change set that improves clarity, safety, operability, and long-term maintainability.

## Workflow

- start from the owning feature folder or route
- keep composables honest about the state they own
- protect route and event semantics during refactors
- verify the Vite build and test path after changes

## Typical Focus Areas

- Vue version and host environment
- Composition API, Options API, or mixed posture
- router and store strategy
- app, library, or admin-surface scope

## Outputs to Prefer

- summarize API posture and host environment first
- group findings by components, composables, state, routing, and tests
- recommend feature-by-feature modernization instead of broad rewrites

## First Response Pattern

- restate Vue version, API posture, and router or store strategy before suggesting changes
- anchor the plan at the owning feature, route, composable, or store boundary
- name the verification loop up front: `npm run test`, `npm run build`, and a smoke test of the affected route or state flow

## Common Requests

```text
Review this Vue feature for component structure, Composition API or composable usage, Pinia state ownership, routing, and test gaps.
```

```text
Refactor this Vue workflow to simplify composable or store ownership and preserve router and component behavior.
```

## Safety Notes

- preserve externally visible behavior unless the user explicitly requests a redesign or a breaking change
- avoid style-only churn when the current repository already has working conventions and automation
