---
name: express-js
description: >
  review, design, scaffold, refactor, and troubleshoot express.js applications and apis. use when the user asks for express routing, middleware, validation, error handling, session or auth design, testing, security hardening, or migration guidance.
---

# Express.js

Use this skill to keep Express.js work grounded in maintainable architecture, predictable delivery, and framework-appropriate conventions.

## Intent Router

| Need | Load |
| --- | --- |
| core conventions, structure, review priorities, and common red flags for Express.js | `references/best-practices.md` |
| setup, migration, testing, build, delivery, and day-two workflow guidance for Express.js | `references/workflows.md` |

## Quick Start

1. Confirm Express and Node versions, API-only or mixed web-app scope, auth and session posture, and deployment and reverse-proxy model.
2. Identify whether the task is greenfield scaffolding, incremental refactoring, troubleshooting, migration planning, or code review.
3. Apply the defaults in `references/best-practices.md` before proposing custom architecture.
4. Prefer the smallest change set that improves clarity, safety, operability, and long-term maintainability.

## Workflow

- start from router ownership and middleware order
- validate input before business logic runs
- separate HTTP concerns from domain workflows
- verify startup, health checks, and proxy assumptions after changes

## Typical Focus Areas

- Express and Node versions
- API-only or mixed web-app scope
- auth and session posture
- deployment and reverse-proxy model

## Outputs to Prefer

- summarize deployment, auth, and middleware constraints first
- group findings by routes, middleware order, validation, errors, and security posture
- protect public route contracts during cleanup

## First Response Pattern

- restate the Express and Node versions, app scope, auth posture, and proxy assumptions before suggesting changes
- anchor the plan at router ownership and middleware order before changing handlers
- name the verification loop up front: local server start, route exercise with representative validation or auth paths, and health-check confirmation

## Common Requests

```text
Review this Express.js API for router structure, middleware ordering, validation, and error handling.
```

```text
Help refactor an Express service toward cleaner transport boundaries and safer request handling.
```

## Safety Notes

- preserve externally visible behavior unless the user explicitly requests a redesign or a breaking change
- avoid style-only churn when the current repository already has working conventions and automation
