# Laravel best practices

## Scope

- confirm Laravel and PHP version
- confirm Blade, API, Livewire, Inertia, or hybrid delivery model
- confirm database and queue posture
- confirm deployment style

## Default design choices

- Keep controllers thin and use form requests for boundary validation where they fit naturally.
- Use Eloquent deliberately and add mapping layers when transport needs diverge from persistence shape.
- Keep jobs and queue handlers focused on one durable unit of work.
- Centralize authorization and configuration behavior instead of scattering it.

## Common red flags

- controllers performing validation, auth, persistence, and response shaping together
- models carrying hidden cross-cutting workflow logic
- jobs that depend on ambient request state
- config or env reads spread through business code

## Review checklist

- [ ] delivery model and queue posture are clear
- [ ] routes, validation, and auth boundaries are explicit
- [ ] Eloquent and transaction behavior are intentional
- [ ] deployment-sensitive config and worker assumptions are visible

## Migration playbook

- stabilize request validation and authorization boundaries first
- add feature tests around important routes and jobs
- extract multi-step workflows out of controllers or model events incrementally
