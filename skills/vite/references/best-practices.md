# Vite best practices

## Scope

- confirm Vite version and framework plugin stack
- confirm dev-server versus build-time problem scope
- confirm artifact type: app, library, or docs site
- confirm deployment target and env strategy

## Default design choices

- Keep config small and explicit; prefer documented defaults over abstraction sprawl.
- Use import.meta.env carefully and document which variables are intentionally public.
- Prefer manual chunking only when bundle analysis shows a real need.
- Align Vite, Vitest, and framework aliases so local and CI behavior stay predictable.

## Common red flags

- plugin chains that depend on order but are undocumented
- different alias or env behavior between Vite, Vitest, and TS config
- HMR-only fixes masking preview or production build issues
- public env prefixes that expose secrets

## Review checklist

- [ ] Vite version and plugin stack are clear
- [ ] config changes solve the right layer
- [ ] env exposure is explicit and safe
- [ ] output and preview behavior remain predictable

## Migration playbook

- match entry points, aliases, and env expectations first
- migrate a simple feature path first to validate plugin and asset assumptions
- add rollup-level customization only after the baseline migration is stable
