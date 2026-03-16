# React best practices

## Scope

- confirm React version and host framework
- confirm client-only or server-rendered delivery
- confirm local state, context, reducer, or store posture
- confirm design-system or product-app scope

## Default design choices

- Keep state as local as practical and lift only when multiple consumers truly need it.
- Use hooks to clarify behavior, not to hide incidental complexity.
- Prefer accessible, explicit component APIs over clever abstraction.
- Measure performance before adding memoization or heavy optimization layers.

## Common red flags

- components that fetch data, manage forms, and render complex UI all in one file
- custom hooks with hidden mutable module state
- context created for narrow local concerns
- memoization added everywhere with no evidence of render pressure

## Review checklist

- [ ] host environment and rendering model are clear
- [ ] component and prop boundaries stay small
- [ ] state ownership and side effects are easy to trace
- [ ] accessibility and interaction behavior remain testable

## Migration playbook

- split oversized components first
- move side effects into explicit adapters or focused hooks
- replace broad context or store usage with narrower ownership when it simplifies reasoning
