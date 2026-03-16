# Vue best practices

## Scope

- confirm Vue version and host environment
- confirm Composition API, Options API, or mixed posture
- confirm router and store strategy
- confirm app, library, or admin-surface scope

## Default design choices

- Use Composition API for new work unless the repository is intentionally standardized otherwise.
- Keep composables focused on one concern and avoid hidden singleton state.
- Prefer local state first and then Pinia for durable shared concerns.
- Keep SFC sections disciplined and easy to scan.

## Common red flags

- composables that mutate hidden shared state everywhere
- components mixing network calls, validation, permissions, and rendering
- props copied into local refs and manually synchronized without clear reason
- stores becoming dumping grounds for transient UI state

## Review checklist

- [ ] Vue version, host environment, and API posture are clear
- [ ] component and composable responsibilities stay small
- [ ] state ownership is explicit and not overly centralized
- [ ] routing and forms remain testable

## Migration playbook

- stabilize component contracts and store boundaries first
- extract large reusable logic into focused composables
- migrate feature by feature rather than rewriting the full app posture
