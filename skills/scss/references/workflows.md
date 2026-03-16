# SCSS workflows

## Establish the target

- confirm Sass compiler and module system
- confirm global styles, CSS modules, or scoped-style consumption model
- confirm design-token source
- confirm runtime theming requirements

## Day-two workflow

- start from token sources and entry-point stylesheets
- flatten the highest-risk selectors first
- keep compile-time and runtime theming responsibilities distinct
- inspect compiled CSS and screenshots after structural changes

## Common commands

```bash
sass src/styles:dist/styles --update
npm run build
```

```bash
sass --watch src/styles:dist/styles
npm run lint:styles
```

## Verification

- compile the affected styles through the host build or Sass CLI and inspect the output for selector drift, duplicate rules, or namespace mistakes
- confirm tokens, mixins, and module exports still resolve through `@use` or `@forward` without reviving deprecated global imports
- check one real page or component for cascade leaks, responsive regressions, and dark-mode or theme regressions after the change

## Troubleshooting and recovery

- if a migration from `@import` to `@use` breaks variables or mixins, fix namespace references before reaching for duplicated compatibility shims
- if the cascade becomes unstable, move shared tokens upward and narrow selectors rather than adding more specificity
- if generated CSS balloons, look for repeated utility generation, duplicated forwards, or theme maps emitted in many entry points
