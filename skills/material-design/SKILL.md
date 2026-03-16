---
name: material-design
description: >
  review, design, and implement material design based interfaces and design systems. use when the user asks for material design or material 3 guidance, theming, design tokens, component selection, density, accessibility, motion, or framework-specific material library integration.
---

# Material Design

Use this skill to keep Material Design work grounded in maintainable architecture, predictable delivery, and framework-appropriate conventions.

## Intent Router

| Need | Load |
| --- | --- |
| core conventions, structure, review priorities, and common red flags for Material Design | `references/best-practices.md` |
| setup, migration, testing, build, delivery, and day-two workflow guidance for Material Design | `references/workflows.md` |

## Quick Start

1. Confirm product context and target platform, component library choice such as Angular Material, MUI, or Material Web, token and theme system, and brand latitude and accessibility requirements.
2. Identify whether the task is greenfield scaffolding, incremental refactoring, troubleshooting, migration planning, or code review.
3. Apply the defaults in `references/best-practices.md` before proposing custom architecture.
4. Prefer the smallest change set that improves clarity, safety, operability, and long-term maintainability.

## Workflow

- start from tokens and hierarchy before polishing visual details
- map generic guidance into the chosen library carefully
- review navigation, state feedback, and accessibility together
- use screenshots or previews for shared theme changes

## Typical Focus Areas

- product context and target platform
- component library choice such as Angular Material, MUI, or Material Web
- token and theme system
- brand latitude and accessibility requirements

## Outputs to Prefer

- summarize platform, library, and token constraints first
- group findings by tokens, hierarchy, component fit, and accessibility
- document intentional divergence from stock Material guidance

## First Response Pattern

- restate the target platform, component library, token system, and accessibility constraints before suggesting changes
- anchor the plan at tokens, hierarchy, and interaction states before discussing visual polish
- name the verification loop up front: preview or Storybook review, keyboard and contrast checks, and screenshot comparison for shared theme changes

## Common Requests

```text
Review this Material 3 dashboard plan for hierarchy, token mapping, density, accessibility, and component selection across MUI, Angular Material, or Material Web. The repo already has a dark theme and Storybook snapshots, and the goal is to reduce visual noise without rewriting every component.
```

```text
Help map Material 3 color, typography, shape, and motion tokens into an existing MUI or Angular Material library for a settings surface, while preserving keyboard behavior, focus states, and current screenshot-based regression checks.
```

## Safety Notes

- preserve externally visible behavior unless the user explicitly requests a redesign or a breaking change
- avoid style-only churn when the current repository already has working conventions and automation
