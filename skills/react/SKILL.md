---
name: react
description: >
  review, design, scaffold, refactor, and troubleshoot react applications and component libraries. use when the user asks for react component design, hooks, state ownership, context, rendering patterns, testing, performance tradeoffs, or migration guidance.
---

# React

Use this skill to keep React work grounded in maintainable architecture, predictable delivery, and framework-appropriate conventions.

## Intent Router

| Need | Load |
| --- | --- |
| core conventions, structure, review priorities, and common red flags for React | `references/best-practices.md` |
| setup, migration, testing, build, delivery, and day-two workflow guidance for React | `references/workflows.md` |

## Quick Start

1. Confirm React version and host framework, client-only or server-rendered delivery, local state, context, reducer, or store posture, and design-system or product-app scope.
2. Identify whether the task is greenfield scaffolding, incremental refactoring, troubleshooting, migration planning, or code review.
3. Apply the defaults in `references/best-practices.md` before proposing custom architecture.
4. Prefer the smallest change set that improves clarity, safety, operability, and long-term maintainability.

## Workflow

- start from the owning feature or component boundary
- keep effects narrow and traceable
- test user-visible behavior instead of implementation detail
- verify host-framework build and test paths after changes

## Typical Focus Areas

- React version and host framework
- client-only or server-rendered delivery
- local state, context, reducer, or store posture
- design-system or product-app scope

## Outputs to Prefer

- summarize rendering host and state posture first
- group findings by component boundaries, state ownership, accessibility, and tests
- recommend concrete refactors that preserve public component contracts

## First Response Pattern

- restate the host framework, rendering model, and state ownership posture before suggesting changes
- anchor the plan at the owning component or feature boundary instead of broad abstraction churn
- name the verification loop up front: host build or test commands plus a smoke test of the affected interaction

## Common Requests

```text
Review this React component tree for state ownership, hook usage, accessibility, and test gaps.
```

```text
Refactor this React feature to simplify composition and reduce incidental re-renders without changing behavior.
```

## Safety Notes

- preserve externally visible behavior unless the user explicitly requests a redesign or a breaking change
- avoid style-only churn when the current repository already has working conventions and automation
