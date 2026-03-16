# NextJS best practices

## Scope

- confirm Next.js version and router model
- confirm Node versus Edge runtime targets
- confirm SSR, SSG, streaming, or authenticated app shell
- confirm cache, revalidation, and mutation model

## Default design choices

- Use App Router for new work unless the repository is intentionally standardized otherwise.
- Keep data fetching server-first when it reduces client bundle size and secret exposure.
- Co-locate layouts, metadata, loading, and error ownership with the route tree that owns them.
- Treat cache invalidation as part of the feature design, especially after mutations.

## Common red flags

- client components fetching data already available to server components
- route handlers mixing validation, auth, persistence, and response shaping
- implicit cache behavior after mutations
- runtime boundaries that expose secrets or enlarge bundles

## Review checklist

- [ ] router model and runtime target are clear
- [ ] server and client boundaries are intentional
- [ ] mutations and revalidation paths are explicit
- [ ] metadata and loading or error ownership are clear

## Migration playbook

- stabilize route ownership and data access first
- move reusable logic into server-safe libraries before changing route trees
- migrate leaf routes incrementally instead of rewriting the whole app
