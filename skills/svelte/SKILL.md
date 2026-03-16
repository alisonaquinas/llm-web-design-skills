---
name: svelte
description: >
  review, design, scaffold, refactor, and troubleshoot svelte applications and component libraries. use when the user asks for svelte reactivity, component design, stores, sveltekit routing or loading, forms, transitions, testing, or migration guidance.
---

# Svelte

Use this skill to keep Svelte work grounded in maintainable architecture, predictable delivery, and framework-appropriate conventions.

## Intent Router

| Need | Load |
| --- | --- |
| core conventions, structure, review priorities, and common red flags for Svelte | `references/best-practices.md` |
| setup, migration, testing, build, delivery, and day-two workflow guidance for Svelte | `references/workflows.md` |

## Quick Start

1. Confirm Svelte version and whether SvelteKit is in scope, client-only, SSR, SSG, or hybrid rendering, runes, stores, or mixed migration posture, and adapter and deployment target.
2. Identify whether the task is greenfield scaffolding, incremental refactoring, troubleshooting, migration planning, or code review.
3. Apply the defaults in `references/best-practices.md` before proposing custom architecture.
4. Prefer the smallest change set that improves clarity, safety, operability, and long-term maintainability.

## Workflow

- start from the owner of data and route behavior
- keep server and client boundaries explicit when SvelteKit is involved
- preserve progressive enhancement and accessibility
- verify the adapter build and preview path after changes

## Typical Focus Areas

- Svelte version and whether SvelteKit is in scope
- client-only, SSR, SSG, or hybrid rendering
- runes, stores, or mixed migration posture
- adapter and deployment target

## Outputs to Prefer

- summarize version, host, and adapter assumptions first
- group findings by reactivity, route ownership, forms, and delivery risk
- prefer incremental cleanup over changing posture everywhere at once

## First Response Pattern

- restate whether SvelteKit is in scope, the rendering mode, and the adapter target before suggesting changes
- anchor the plan at the owning route, load function, action, or component boundary
- name the verification loop up front: `npm run check`, `npm run test`, `npm run build`, and a preview check of the affected route

## Common Requests

```text
Review this Svelte or SvelteKit feature for reactivity, load boundaries, accessibility, and test gaps.
```

```text
Refactor this Svelte flow to simplify state handling and preserve user-visible behavior.
```

## Safety Notes

- preserve externally visible behavior unless the user explicitly requests a redesign or a breaking change
- avoid style-only churn when the current repository already has working conventions and automation
