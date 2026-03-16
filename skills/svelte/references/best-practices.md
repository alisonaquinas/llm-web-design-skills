# Svelte best practices

## Scope

- confirm Svelte version and whether SvelteKit is in scope
- confirm client-only, SSR, SSG, or hybrid rendering
- confirm runes, stores, or mixed migration posture
- confirm adapter and deployment target

## Default design choices

- Keep reactivity obvious and avoid derived-state chains that hide ownership.
- Use shared stores only when multiple branches truly need them.
- Use route-level loading or actions when SvelteKit owns the request lifecycle.
- Use transitions only when they communicate state change and do not harm accessibility.

## Common red flags

- duplicating server-loaded data into writable stores without a reason
- route files mixing auth, validation, persistence, and presentation heavily
- reactive statements with hidden mutation or ordering assumptions
- form actions with no progressive enhancement story

## Review checklist

- [ ] Svelte version, host, and adapter target are clear
- [ ] reactivity and shared state ownership are easy to explain
- [ ] server and client boundaries are explicit
- [ ] progressive enhancement remains intact

## Migration playbook

- stabilize route ownership first
- move large scripts into shared modules before reorganizing components
- standardize on one reactive posture per area where possible
