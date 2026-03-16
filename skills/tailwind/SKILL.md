---
name: tailwind
description: >
  review, design, scaffold, refactor, and troubleshoot tailwind css based styling systems. use when the user asks for tailwind configuration, utility usage, design tokens, component extraction, theming, responsive patterns, or migration guidance.
---

# Tailwind

Use this skill to keep Tailwind work grounded in maintainable architecture, predictable delivery, and framework-appropriate conventions.

## Intent Router

| Need | Load |
| --- | --- |
| core conventions, structure, review priorities, and common red flags for Tailwind | `references/best-practices.md` |
| setup, migration, testing, build, delivery, and day-two workflow guidance for Tailwind | `references/workflows.md` |

## Quick Start

1. Confirm Tailwind version and framework host, theme and token strategy, dark-mode posture, and direct-utility versus extracted-component boundary.
2. Identify whether the task is greenfield scaffolding, incremental refactoring, troubleshooting, migration planning, or code review.
3. Apply the defaults in `references/best-practices.md` before proposing custom architecture.
4. Prefer the smallest change set that improves clarity, safety, operability, and long-term maintainability.

## Workflow

- start from semantic tokens and then map utilities onto them
- review responsive, dark, focus, and loading states together
- extract shared recipes only after duplication is real
- verify scanning paths and production build size after config changes

## Typical Focus Areas

- Tailwind version and framework host
- theme and token strategy
- dark-mode posture
- direct-utility versus extracted-component boundary

## Outputs to Prefer

- summarize host framework and token strategy first
- group findings by theme config, utility composition, extracted recipes, and responsive or dark behavior
- prefer token cleanup before helper-library proliferation

## First Response Pattern

- restate Tailwind version, host framework, token strategy, and dark-mode posture before suggesting changes
- anchor the plan at theme tokens, utility usage, and the smallest shared recipe that actually needs extraction
- name the verification loop up front: host build, responsive and dark-state inspection, and generated CSS or content-scan confirmation

## Common Requests

```text
Review this Tailwind component set for utility readability, theme-token discipline, responsive and dark-mode behavior, and maintainability in a React or Vue app that already ships with `npm run build` and visual smoke tests.
```

```text
Help structure Tailwind config, content scanning, and shared utility recipes for a larger design system where repeated card, button, and form patterns are drifting across multiple packages.
```

## Safety Notes

- preserve externally visible behavior unless the user explicitly requests a redesign or a breaking change
- avoid style-only churn when the current repository already has working conventions and automation
