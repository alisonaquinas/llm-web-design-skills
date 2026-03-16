# Material Design best practices

## Scope

- confirm product context and target platform
- confirm component library choice such as Angular Material, MUI, or Material Web
- confirm token and theme system
- confirm brand latitude and accessibility requirements

## Default design choices

- Start from Material 3 token roles and map them into the real implementation layer.
- Choose components based on task fit and information hierarchy, not visual novelty.
- Keep spacing, density, motion, and elevation consistent across feature areas.
- Treat focus, keyboard interaction, contrast, and reduced motion as first-class requirements.

## Common red flags

- multiple competing emphasis systems fighting for attention
- theme overrides scattered through product code
- customized components that break focus or semantic behavior
- dark mode implemented as ad hoc color swaps

## Review checklist

- [ ] target product context and library are clear
- [ ] theme roles and contrast are deliberate
- [ ] component choices match task complexity
- [ ] motion and elevation reinforce meaning instead of noise

## Migration playbook

- centralize tokens first
- normalize navigation and page hierarchy before component restyling
- migrate shared primitives before feature-specific overrides
