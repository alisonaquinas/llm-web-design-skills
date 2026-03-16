---
name: asp-net
description: >
  review, design, scaffold, refactor, and troubleshoot asp.net core applications. use when the user asks for asp.net api design, minimal apis, mvc or razor pages, dependency injection, middleware, configuration, ef core integration, testing, or deployment guidance.
---

# ASP.NET

Use this skill to keep ASP.NET work grounded in maintainable architecture, predictable delivery, and framework-appropriate conventions.

## Intent Router

| Need | Load |
| --- | --- |
| core conventions, structure, review priorities, and common red flags for ASP.NET | `references/best-practices.md` |
| setup, migration, testing, build, delivery, and day-two workflow guidance for ASP.NET | `references/workflows.md` |

## Quick Start

1. Confirm .NET and ASP.NET Core version, Minimal APIs, MVC, Razor Pages, or hybrid posture, hosting and deployment model, and data-access and background-work posture.
2. Identify whether the task is greenfield scaffolding, incremental refactoring, troubleshooting, migration planning, or code review.
3. Apply the defaults in `references/best-practices.md` before proposing custom architecture.
4. Prefer the smallest change set that improves clarity, safety, operability, and long-term maintainability.

## Workflow

- start from the composition root and public contracts
- keep config and service registration explicit
- separate transport, application logic, and infrastructure
- verify build, tests, and startup after changes

## Typical Focus Areas

- .NET and ASP.NET Core version
- Minimal APIs, MVC, Razor Pages, or hybrid posture
- hosting and deployment model
- data-access and background-work posture

## Outputs to Prefer

- summarize hosting style and application type first
- group findings by middleware, DI, config, endpoints, persistence, and tests
- protect public routes and deployment assumptions during cleanup

## First Response Pattern

- restate the .NET and ASP.NET Core version, hosting posture, and data or background-work model before suggesting changes
- anchor the plan at the composition root, middleware, and public endpoint contracts
- name the verification loop up front: `dotnet build`, `dotnet test`, `dotnet run`, and one representative request or startup path

## Common Requests

```text
Review this ASP.NET Core service for endpoint design, middleware order, DI usage, and test gaps.
```

```text
Help refactor an ASP.NET codebase toward cleaner hosting and application boundaries.
```

## Safety Notes

- preserve externally visible behavior unless the user explicitly requests a redesign or a breaking change
- avoid style-only churn when the current repository already has working conventions and automation
