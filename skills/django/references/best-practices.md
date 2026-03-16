# Django best practices

## Scope

- confirm Django and Python versions
- confirm template-driven, API-driven, or hybrid delivery
- confirm database backend
- confirm background-task or async posture

## Default design choices

- Keep each Django app cohesive around a business capability.
- Use forms, serializers, or dedicated validators to validate external input at the boundary.
- Keep settings modular and environment-aware.
- Use explicit orchestration for multi-step workflows spanning many models or external systems.

## Common red flags

- fat models, fat views, and unowned domain rules split across both
- signals used for core workflows that should be explicit orchestration
- settings imported broadly with runtime side effects
- migrations without a safe rollout plan

## Review checklist

- [ ] delivery model and database assumptions are clear
- [ ] apps, models, views, and services have intentional ownership
- [ ] validation, permissions, and transactions are explicit
- [ ] settings and secret management are deployment-safe

## Migration playbook

- stabilize settings and environment boundaries first
- write tests around forms, serializers, permissions, and migrations before refactors
- decompose legacy apps by capability over time
