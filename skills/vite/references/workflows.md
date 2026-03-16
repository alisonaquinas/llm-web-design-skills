# Vite workflows

## Establish the target

- confirm Vite version and framework plugin stack
- confirm dev-server versus build-time problem scope
- confirm artifact type: app, library, or docs site
- confirm deployment target and env strategy

## Day-two workflow

- identify whether the problem is in dev, build, preview, or tests
- keep alias and env naming aligned across tools
- separate functional correctness from performance tuning
- verify preview and production-like behavior after config changes

## Concrete scenario patterns

### Resolve dev-versus-preview drift

- reproduce the issue in `npm run dev`, then compare the same route or asset in `npm run preview`
- inspect alias resolution, asset paths, and environment loading before changing application code
- keep the first fix at the Vite config seam unless the bug is clearly inside the app itself

### Migrate a webpack or CRA entry point incrementally

- move aliases, env handling, and one representative feature path first
- validate plugin behavior with both `npm run build` and `npx vitest run`
- add manual chunking or advanced Rollup options only after the baseline migration is stable

## Common commands

```bash
npm run dev
npm run build
npm run preview
```

```bash
npm run test
npx vitest run
```

## Verification

- run `npm run dev`, `npm run build`, and `npm run test` or `npm run preview` to confirm the changed setup still works in both dev and production-like flows
- verify aliasing, plugin hooks, environment variables, and asset handling from the browser entry point instead of assuming the config stayed valid
- confirm hot-module replacement behavior only after the production build is known-good
- compare at least one real route, asset, or test path before and after the config change so preview parity is explicit

## Troubleshooting and recovery

- if the build breaks after config edits, revert to the last known-good plugin or alias change and reintroduce one option at a time
- if environment values disappear, compare `import.meta.env` usage, mode-specific files, and server-only assumptions first
- if dev and build differ, inspect plugin ordering, SSR flags, and asset import paths before rewriting the application code
- if migration churn spreads too broadly, freeze on the last stable entry path and finish one vertical slice before touching more build knobs
