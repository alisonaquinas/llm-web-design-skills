# SCSS best practices

## Scope

- confirm Sass compiler and module system
- confirm global styles, CSS modules, or scoped-style consumption model
- confirm design-token source
- confirm runtime theming requirements

## Default design choices

- Prefer the modern Sass module system with @use and @forward over global @import patterns.
- Centralize tokens and separate semantic tokens from raw palette primitives.
- Use nesting sparingly and stop when selectors become hard to read or override.
- Use CSS custom properties when runtime theme switching is required and SCSS for compile-time organization.

## Common red flags

- deep nesting that encodes DOM structure
- global partials leaking variables and mixins everywhere
- mixin overuse that obscures the generated CSS
- specificity battles solved with more nesting or !important

## Review checklist

- [ ] compiler and module system are clear
- [ ] tokens and theme layers are centralized
- [ ] nesting and specificity remain easy to reason about
- [ ] mixins and functions simplify rather than obscure

## Migration playbook

- centralize tokens first
- replace @import with module-system boundaries incrementally
- introduce CSS variables where runtime theming is needed
