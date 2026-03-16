# Angular best practices

## Scope

- confirm Angular version and workspace toolchain
- confirm standalone APIs versus NgModules
- confirm SSR, SSG, or client-only rendering
- confirm signals, RxJS, or store posture

## Default design choices

- Prefer standalone features for new work unless the repository is standardized on NgModules.
- Use signals for local synchronous UI state and RxJS for async or multi-source flows.
- Keep templates declarative and move complex branching into computed state or helpers.
- Prefer reactive forms for non-trivial workflows and shared validation.

## Common red flags

- manual subscriptions with unclear teardown
- templates that duplicate business rules
- services with hidden app-wide mutation
- route or form behavior spread across many unrelated files

## Review checklist

- [ ] version, rendering mode, and workspace shape are known
- [ ] component, service, and route responsibilities are separated
- [ ] signals, RxJS, and forms are each used for the jobs they fit best
- [ ] loading, empty, and error states remain visible and testable

## Migration playbook

- stabilize routing and data-loading seams first
- introduce standalone features at boundaries instead of rewriting everything
- add focused tests around forms and route transitions before major refactors
