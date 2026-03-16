---
name: scss
description: >
  review, design, scaffold, refactor, and troubleshoot scss and sass based styling systems. use when the user asks for scss architecture, variables and tokens, mixins, nesting, partials, modules, theming, build integration, or migration guidance.
---

# SCSS

Use this skill to keep SCSS work grounded in maintainable architecture, predictable delivery, and framework-appropriate conventions.

## Intent Router

| Need | Load |
| --- | --- |
| core conventions, structure, review priorities, and common red flags for SCSS | `references/best-practices.md` |
| setup, migration, testing, build, delivery, and day-two workflow guidance for SCSS | `references/workflows.md` |

## Quick Start

1. Confirm Sass compiler and module system, global styles, CSS modules, or scoped-style consumption model, design-token source, and runtime theming requirements.
2. Identify whether the task is greenfield scaffolding, incremental refactoring, troubleshooting, migration planning, or code review.
3. Apply the defaults in `references/best-practices.md` before proposing custom architecture.
4. Prefer the smallest change set that improves clarity, safety, operability, and long-term maintainability.

## Workflow

- start from token sources and entry-point stylesheets
- flatten the highest-risk selectors first
- keep compile-time and runtime theming responsibilities distinct
- inspect compiled CSS and screenshots after structural changes

## Typical Focus Areas

- Sass compiler and module system
- global styles, CSS modules, or scoped-style consumption model
- design-token source
- runtime theming requirements

## Outputs to Prefer

- summarize compiler, consumption model, and token posture first
- group findings by modules, tokens, nesting, theming, and build integration
- recommend architecture cleanup before cosmetic churn

## First Response Pattern

- restate the Sass module system, stylesheet consumption model, and runtime theming requirements before suggesting changes
- anchor the plan at token sources, entry-point stylesheets, and the narrowest selector boundary
- name the verification loop up front: Sass compile or host build, compiled CSS inspection, and a screenshot check of the affected page or component

## Common Requests

```text
Review this SCSS structure for module boundaries, nesting discipline, token usage, and override risk.
```

```text
Help refactor a legacy Sass codebase into a more maintainable token and partial architecture.
```

## Safety Notes

- preserve externally visible behavior unless the user explicitly requests a redesign or a breaking change
- avoid style-only churn when the current repository already has working conventions and automation
