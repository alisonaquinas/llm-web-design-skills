---
name: hugo
description: >
  review, design, scaffold, refactor, and troubleshoot hugo sites and themes. use when the user asks for hugo content structure, layouts, taxonomies, shortcodes, themes, assets, build configuration, multilingual publishing, or migration guidance.
---

# Hugo

Use this skill to keep Hugo work grounded in maintainable architecture, predictable delivery, and framework-appropriate conventions.

## Intent Router

| Need | Load |
| --- | --- |
| core conventions, structure, review priorities, and common red flags for Hugo | `references/best-practices.md` |
| setup, migration, testing, build, delivery, and day-two workflow guidance for Hugo | `references/workflows.md` |

## Quick Start

1. Confirm Hugo version and theme posture, content bundle strategy, multilingual or taxonomy needs, and deployment host and URL constraints.
2. Identify whether the task is greenfield scaffolding, incremental refactoring, troubleshooting, migration planning, or code review.
3. Apply the defaults in `references/best-practices.md` before proposing custom architecture.
4. Prefer the smallest change set that improves clarity, safety, operability, and long-term maintainability.

## Workflow

- start from content ownership and URL strategy
- keep layouts layered and override-friendly
- document shortcode and taxonomy rules
- verify local preview and deploy output after structural changes

## Typical Focus Areas

- Hugo version and theme posture
- content bundle strategy
- multilingual or taxonomy needs
- deployment host and URL constraints

## Outputs to Prefer

- summarize theme, content-model, and deployment constraints first
- group findings by content bundles, layouts, shortcodes, taxonomies, and publishing flow
- protect URLs and editorial workflows during cleanup

## First Response Pattern

- restate the Hugo version, theme posture, content-bundle model, and deployment URL constraints before suggesting changes
- anchor the plan at content ownership, layout override order, and URL strategy
- name the verification loop up front: `hugo server`, `hugo --gc --minify`, and inspection of the affected generated URLs and assets

## Common Requests

```text
Review this Hugo site structure for content modeling, layouts, shortcodes, and build hygiene.
```

```text
Help refactor a Hugo site toward clearer content bundles and easier theme overrides.
```

## Safety Notes

- preserve externally visible behavior unless the user explicitly requests a redesign or a breaking change
- avoid style-only churn when the current repository already has working conventions and automation
