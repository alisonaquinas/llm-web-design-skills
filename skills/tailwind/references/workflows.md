# Tailwind workflows

## Establish the target

- confirm Tailwind version and framework host
- confirm theme and token strategy
- confirm dark-mode posture
- confirm direct-utility versus extracted-component boundary

## Day-two workflow

- start from semantic tokens and then map utilities onto them
- review responsive, dark, focus, and loading states together
- extract shared recipes only after duplication is real
- verify scanning paths and production build size after config changes

## Concrete scenario patterns

### Audit a drifting component set

- review one button, one card, and one form control across mobile, desktop, and dark mode
- list arbitrary values that should become tokens before proposing recipe extraction
- keep the first cleanup inside the existing host framework instead of introducing another class-merging helper

### Fix missing classes in production builds

- compare a failing production route with the local development view
- inspect `content` globs, safelists, and generated CSS before changing markup
- rerun the Tailwind CLI build and confirm the missing utilities now appear in the compiled output

## Common commands

```bash
npm run dev
npm run build
```

```bash
npx tailwindcss -i ./src/input.css -o ./dist/output.css --minify
npm run lint
```

## Verification

- run the host build or `npx tailwindcss -i ./src/input.css -o ./dist/output.css --minify`, then inspect the affected UI for responsive, dark, focus, disabled, and loading states
- confirm the generated CSS still reflects the intended content-scanning paths and does not miss templates or emit accidental bloat
- verify that repeated arbitrary values were either preserved intentionally or promoted into durable theme tokens
- confirm extracted recipes did not hide state logic that was clearer when left as direct utilities

## Troubleshooting and recovery

- if styles disappear, check content globs, safelists, and generated class names before editing component markup
- if utility strings become unreadable, extract only the repeated pattern or variant recipe instead of hiding every class behind abstraction
- if dark mode or responsive behavior drifts, compare the variant strategy and token source before adding more overrides
- if one package in a monorepo behaves differently, compare its Tailwind entry file, config resolution path, and shared preset version before assuming the markup is wrong
