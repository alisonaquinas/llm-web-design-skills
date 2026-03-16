# Angular workflows

## Establish the target

- confirm Angular version and workspace toolchain
- confirm standalone APIs versus NgModules
- confirm SSR, SSG, or client-only rendering
- confirm signals, RxJS, or store posture

## Day-two workflow

- identify feature ownership before editing local files
- separate framework defaults from UI-kit or backend-specific choices
- protect routes, forms, and template behavior during refactors
- verify build and tests after structural changes

## Common commands

```bash
ng serve
ng test
ng build
```

```bash
ng update @angular/core @angular/cli
ng generate component features/orders/order-list
```

## Verification

- run `ng build` and `ng test` after structural changes, then smoke-test the affected routes, forms, and loading or error states
- confirm standalone imports, route providers, and signal or RxJS boundaries still line up with the owning feature
- check rendered templates for accessibility regressions such as missing labels, focus traps, or hidden validation feedback

## Troubleshooting and recovery

- if templates fail after a refactor, inspect standalone imports, directive availability, and signal-versus-observable boundaries first
- if route behavior drifts, compare route configuration, guards, resolvers, and route-level providers before rewriting components
- if SSR or hydration breaks, isolate browser-only code, defer DOM access, and re-test the smallest affected route
