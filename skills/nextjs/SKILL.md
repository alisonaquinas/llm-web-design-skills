---
name: nextjs
description: >
  review, design, scaffold, refactor, and troubleshoot nextjs applications. use when the user asks for nextjs app router structure, server and client component boundaries, routing, data fetching, caching, route handlers, metadata, deployment, or migration guidance.
---

# NextJS

Use this skill to keep NextJS work grounded in maintainable architecture, predictable delivery, and framework-appropriate conventions.

## Intent Router

| Need | Load |
| --- | --- |
| core conventions, structure, review priorities, and common red flags for NextJS | `references/best-practices.md` |
| setup, migration, testing, build, delivery, and day-two workflow guidance for NextJS | `references/workflows.md` |

## Quick Start

1. Confirm Next.js version and router model, Node versus Edge runtime targets, SSR, SSG, streaming, or authenticated app shell, and cache, revalidation, and mutation model.
2. Identify whether the task is greenfield scaffolding, incremental refactoring, troubleshooting, migration planning, or code review.
3. Apply the defaults in `references/best-practices.md` before proposing custom architecture.
4. Prefer the smallest change set that improves clarity, safety, operability, and long-term maintainability.

## Workflow

- start from the route tree and owning layout
- keep server and client boundaries explicit
- treat cache and revalidation as architecture, not afterthoughts
- verify production build and preview behavior after changes

## Typical Focus Areas

- Next.js version and router model
- Node versus Edge runtime targets
- SSR, SSG, streaming, or authenticated app shell
- cache, revalidation, and mutation model

## Outputs to Prefer

- state router model, runtime, and cache assumptions before detailed advice
- group findings by route ownership, server-client boundary, cache behavior, and deployment risk
- prefer incremental route or boundary cleanup over wholesale rewrites

## First Response Pattern

- restate the router model, runtime target, and cache or revalidation posture before suggesting changes
- anchor the plan at the owning route or layout and keep server-client boundaries explicit
- name the verification loop up front: `npm run build`, `npm run lint`, and a preview check of the affected route

## Common Requests

```text
Review this Next.js App Router feature for server or client boundaries, data fetching, caching, and route structure.
```

```text
Refactor this Next.js route to reduce client-side work while preserving behavior and SEO.
```

## Safety Notes

- preserve externally visible behavior unless the user explicitly requests a redesign or a breaking change
- avoid style-only churn when the current repository already has working conventions and automation
