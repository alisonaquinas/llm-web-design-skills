# Hugo best practices

## Scope

- confirm Hugo version and theme posture
- confirm content bundle strategy
- confirm multilingual or taxonomy needs
- confirm deployment host and URL constraints

## Default design choices

- Use content bundles when pages own related assets.
- Keep layouts layered through base templates, blocks, and partials instead of copying full themes.
- Use archetypes to make front matter consistent.
- Reserve shortcodes for durable authoring patterns, not one-off layout hacks.

## Common red flags

- layouts duplicated wholesale when a block override would suffice
- front matter drift across similar content types
- shortcodes becoming a hidden layout language
- taxonomy or permalink changes made casually without redirect planning

## Review checklist

- [ ] theme strategy and deployment host are clear
- [ ] content model fits the editorial workflow
- [ ] layout and partial overrides stay maintainable
- [ ] URLs, taxonomies, and multilingual behavior are intentional

## Migration playbook

- stabilize content model and permalinks first
- normalize front matter through archetypes or schema
- replace repeated template logic with partials incrementally
