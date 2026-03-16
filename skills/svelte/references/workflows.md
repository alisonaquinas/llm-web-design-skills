# Svelte workflows

## Establish the target

- confirm Svelte version and whether SvelteKit is in scope
- confirm client-only, SSR, SSG, or hybrid rendering
- confirm runes, stores, or mixed migration posture
- confirm adapter and deployment target

## Day-two workflow

- start from the owner of data and route behavior
- keep server and client boundaries explicit when SvelteKit is involved
- preserve progressive enhancement and accessibility
- verify the adapter build and preview path after changes

## Common commands

```bash
npm run dev
npm run test
npm run build
```

```bash
npm run check
npx vite preview
```

## Verification

- run `npm run check`, `npm run test`, and `npm run build`, then exercise the affected route or component in local preview
- confirm load functions, form actions, and store or state boundaries still match the intended server-versus-client split
- verify transitions, accessibility semantics, and pending or error UI remain visible after the refactor

## Troubleshooting and recovery

- if state stops updating, inspect whether a value should stay in `$state`, a store, or a derived value before adding more reactivity glue
- if SvelteKit data flow feels unclear, split `load` ownership and server actions back to the route boundary and retest the smallest route
- if hydration or adapter behavior changes, re-check environment variables, adapter config, and browser-only code paths first
