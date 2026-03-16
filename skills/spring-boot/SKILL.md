---
name: spring-boot
description: >
  review, design, scaffold, refactor, and troubleshoot spring boot applications. use when the user asks for spring boot architecture, starters, controllers, services, configuration, data access, testing, actuator, or deployment guidance.
---

# Spring Boot

Use this skill to keep Spring Boot work grounded in maintainable architecture, predictable delivery, and framework-appropriate conventions.

## Intent Router

| Need | Load |
| --- | --- |
| core conventions, structure, review priorities, and common red flags for Spring Boot | `references/best-practices.md` |
| setup, migration, testing, build, delivery, and day-two workflow guidance for Spring Boot | `references/workflows.md` |

## Quick Start

1. Confirm Spring Boot and Java version, API, MVC, messaging, or hybrid app style, data-access posture, and deployment and operational model.
2. Identify whether the task is greenfield scaffolding, incremental refactoring, troubleshooting, migration planning, or code review.
3. Apply the defaults in `references/best-practices.md` before proposing custom architecture.
4. Prefer the smallest change set that improves clarity, safety, operability, and long-term maintainability.

## Workflow

- start from configuration and bean wiring clarity
- keep controllers and listeners thin
- make transactions, retries, and integration boundaries explicit
- verify build, tests, and deployment packaging after changes

## Typical Focus Areas

- Spring Boot and Java version
- API, MVC, messaging, or hybrid app style
- data-access posture
- deployment and operational model

## Outputs to Prefer

- summarize runtime style, data posture, and config model first
- group findings by config, layering, transactions, actuator, and tests
- protect profile and endpoint behavior during refactors

## First Response Pattern

- restate the Spring Boot and Java version, app style, data posture, and operational model before suggesting changes
- anchor the plan at configuration, bean wiring, controller or service boundaries, and profile behavior
- name the verification loop up front: test suite, one local startup path, and one real request or message flow through the changed behavior

## Common Requests

```text
Review this Spring Boot service for layering, configuration, validation, and operational readiness.
```

```text
Help refactor a Spring Boot app toward clearer controller, service, and persistence boundaries.
```

## Safety Notes

- preserve externally visible behavior unless the user explicitly requests a redesign or a breaking change
- avoid style-only churn when the current repository already has working conventions and automation
