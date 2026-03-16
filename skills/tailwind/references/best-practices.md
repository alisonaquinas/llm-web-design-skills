# Tailwind best practices

## Scope

- confirm Tailwind version and framework host
- confirm theme and token strategy
- confirm dark-mode posture
- confirm direct-utility versus extracted-component boundary

## Default design choices

- Centralize colors, spacing, type, and shadows in the theme instead of repeating arbitrary values.
- Use direct utility composition for simple components and extract recipes only when duplication becomes expensive.
- Keep variants predictable and avoid many competing class-merging strategies.
- Treat focus, disabled, loading, and dark-mode states as part of the core design.

## Common red flags

- markup dominated by arbitrary values that should be theme tokens
- multiple class-composition helpers competing in one repo
- component recipes extracted too early
- content scanning paths that miss templates or bloat builds

## Review checklist

- [ ] Tailwind version and host framework are clear
- [ ] utility usage is readable and token-driven
- [ ] extracted abstractions earn their complexity
- [ ] build scanning and plugin usage stay accurate

## Migration playbook

- define semantic tokens first
- migrate one feature area to consistent utilities before abstracting recipes
- normalize dark mode and responsive conventions early
