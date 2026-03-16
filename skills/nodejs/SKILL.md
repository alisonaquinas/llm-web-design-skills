---
name: nodejs
description: >
  review, design, scaffold, refactor, and troubleshoot nodejs applications and runtime patterns. use when the user asks for nodejs service design, modules, streams, async behavior, configuration, process management, testing, performance, or deployment guidance.
---

# NodeJS

Use this skill to keep NodeJS work grounded in maintainable architecture, predictable delivery, and framework-appropriate conventions.

## Intent Router

| Need | Load |
| --- | --- |
| core conventions, structure, review priorities, and common red flags for NodeJS | `references/best-practices.md` |
| setup, migration, testing, build, delivery, and day-two workflow guidance for NodeJS | `references/workflows.md` |

## Quick Start

1. Confirm Node.js version and module system, artifact type: service, CLI, worker, or library, deployment host, and HTTP-heavy, queue-driven, or stream-processing workload.
2. Identify whether the task is greenfield scaffolding, incremental refactoring, troubleshooting, migration planning, or code review.
3. Apply the defaults in `references/best-practices.md` before proposing custom architecture.
4. Prefer the smallest change set that improves clarity, safety, operability, and long-term maintainability.

## Workflow

- start from startup, transport, and resource ownership
- validate config and untrusted input at the boundary
- keep transport glue separate from core logic
- verify build, tests, and production start commands after changes

## Typical Focus Areas

- Node.js version and module system
- artifact type: service, CLI, worker, or library
- deployment host
- HTTP-heavy, queue-driven, or stream-processing workload

## Outputs to Prefer

- summarize runtime, module, and deployment assumptions first
- group findings by startup, config, async ownership, observability, and tests
- prefer operable services over clever but opaque abstractions

## First Response Pattern

- restate the Node.js version, module system, artifact type, and workload posture before suggesting changes
- anchor the plan at startup, transport, config, and core-logic boundaries instead of broad rewrites
- name the verification loop up front: package tests, normal start command, and one representative request or job flow

## Common Requests

```text
Review this Node.js service for module structure, async behavior, configuration, and test gaps.
```

```text
Help refactor a Node.js codebase toward clearer runtime boundaries and safer shutdown behavior.
```

## Safety Notes

- preserve externally visible behavior unless the user explicitly requests a redesign or a breaking change
- avoid style-only churn when the current repository already has working conventions and automation
