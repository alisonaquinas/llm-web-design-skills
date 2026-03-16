---
name: laravel
description: >
  review, design, scaffold, refactor, and troubleshoot laravel applications. use when the user asks for laravel routes, controllers, requests, eloquent, blade, queues, jobs, configuration, testing, or deployment guidance.
---

# Laravel

Use this skill to keep Laravel work grounded in maintainable architecture, predictable delivery, and framework-appropriate conventions.

## Intent Router

| Need | Load |
| --- | --- |
| core conventions, structure, review priorities, and common red flags for Laravel | `references/best-practices.md` |
| setup, migration, testing, build, delivery, and day-two workflow guidance for Laravel | `references/workflows.md` |

## Quick Start

1. Confirm Laravel and PHP version, Blade, API, Livewire, Inertia, or hybrid delivery model, database and queue posture, and deployment style.
2. Identify whether the task is greenfield scaffolding, incremental refactoring, troubleshooting, migration planning, or code review.
3. Apply the defaults in `references/best-practices.md` before proposing custom architecture.
4. Prefer the smallest change set that improves clarity, safety, operability, and long-term maintainability.

## Workflow

- start from the route group or capability that owns the behavior
- make validation, auth, transactions, and jobs explicit
- separate framework wiring from domain workflows
- verify migrations, tests, workers, and cache commands after changes

## Typical Focus Areas

- Laravel and PHP version
- Blade, API, Livewire, Inertia, or hybrid delivery model
- database and queue posture
- deployment style

## Outputs to Prefer

- summarize delivery model, queue posture, and deployment constraints first
- group findings by routes, validation, Eloquent, jobs, config, and tests
- protect route and queue semantics during refactors

## First Response Pattern

- restate the Laravel and PHP version, delivery model, queue posture, and deployment assumptions before suggesting changes
- anchor the plan at the owning route group, request validation boundary, job, or Eloquent workflow
- name the verification loop up front: `php artisan test`, safe migration checks, and one real route or job flow through the changed behavior

## Common Requests

```text
Review this Laravel feature for route design, controller boundaries, validation, and Eloquent usage.
```

```text
Help refactor a Laravel app toward clearer request handling and safer background workflow design.
```

## Safety Notes

- preserve externally visible behavior unless the user explicitly requests a redesign or a breaking change
- avoid style-only churn when the current repository already has working conventions and automation
