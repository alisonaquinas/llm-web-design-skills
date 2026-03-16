# React workflows

## Establish the target

- confirm React version and host framework
- confirm client-only or server-rendered delivery
- confirm local state, context, reducer, or store posture
- confirm design-system or product-app scope

## Day-two workflow

- start from the owning feature or component boundary
- keep effects narrow and traceable
- test user-visible behavior instead of implementation detail
- verify host-framework build and test paths after changes

## Common commands

```bash
npm run dev
npm run test
npm run build
```

```bash
npx eslint src
npx vitest run
```

## Verification

- run the host-framework build and test path, then inspect the changed component tree through one user-visible flow in the browser or test harness
- confirm state ownership, accessibility semantics, and component contracts still match the original feature boundary
- verify unnecessary re-renders only after correctness is proven, using profiler or targeted logs rather than guesswork

## Troubleshooting and recovery

- if state becomes difficult to trace, move ownership upward or split one overloaded component before introducing more abstractions
- if effects become noisy after the change, reduce dependencies, remove derived-state effects, and re-check the smallest failing path
- if tests are brittle, rewrite them around visible behavior and public props instead of hook internals or implementation detail
