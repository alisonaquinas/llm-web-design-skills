# Vue workflows

## Establish the target

- confirm Vue version and host environment
- confirm Composition API, Options API, or mixed posture
- confirm router and store strategy
- confirm app, library, or admin-surface scope

## Day-two workflow

- start from the owning feature folder or route
- keep composables honest about the state they own
- protect route and event semantics during refactors
- verify the Vite build and test path after changes

## Common commands

```bash
npm run dev
npm run test
npm run build
```

```bash
npm run lint
npx vite preview
```

## Verification

- run `npm run test` and `npm run build`, then smoke-test the changed route, store interaction, or component state flow
- confirm props, emits, composables, and Pinia or router boundaries still align with the owning feature
- check template accessibility, async error handling, and loading states before optimizing composition details

## Troubleshooting and recovery

- if reactivity breaks, inspect `ref`, `reactive`, `computed`, and destructuring choices before layering on watchers
- if routing or store state drifts, move ownership back to the route or store boundary and verify one feature end-to-end
- if component APIs become noisy, simplify props and emits first and defer larger architectural moves until the behavior is stable again
