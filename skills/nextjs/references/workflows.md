# NextJS workflows

## Establish the target

- confirm Next.js version and router model
- confirm Node versus Edge runtime targets
- confirm SSR, SSG, streaming, or authenticated app shell
- confirm cache, revalidation, and mutation model

## Day-two workflow

- start from the route tree and owning layout
- keep server and client boundaries explicit
- treat cache and revalidation as architecture, not afterthoughts
- verify production build and preview behavior after changes

## Common commands

```bash
npm run dev
npm run build
npm run lint
```

```bash
npm run test
npx @next/codemod app-router .
```

## Verification

- run `npm run build` and `npm run lint`, then smoke-test the affected route in preview or production-like mode
- confirm the server or client boundary is still intentional, metadata resolves correctly, and loading or error states still appear
- verify cache invalidation, revalidation, and mutation paths with one real request flow instead of assuming the old behavior still holds

## Troubleshooting and recovery

- if a route suddenly needs client-only code, move only the interactive leaf behind `"use client"` and keep data access server-first where possible
- if stale data appears after mutations, inspect cache tags, `revalidatePath`, `revalidateTag`, and fetch caching options before broad rewrites
- if preview differs from production, compare runtime targets, environment variables, and edge-versus-node assumptions first
