# Hugo workflows

## Establish the target

- confirm Hugo version and theme posture
- confirm content bundle strategy
- confirm multilingual or taxonomy needs
- confirm deployment host and URL constraints

## Day-two workflow

- start from content ownership and URL strategy
- keep layouts layered and override-friendly
- document shortcode and taxonomy rules
- verify local preview and deploy output after structural changes

## Common commands

```bash
hugo server -D
hugo
hugo new posts/my-post.md
```

```bash
hugo --gc --minify
hugo config
```

## Verification

- run `hugo server` for local review and `hugo --gc --minify` for production output, then inspect the affected URLs and generated assets
- confirm layouts, shortcodes, taxonomies, and content bundle assumptions still produce the intended front matter and navigation behavior
- verify canonical URLs, multilingual paths, and asset fingerprints after structural changes

## Troubleshooting and recovery

- if layouts unexpectedly change, walk the theme override chain from the most specific template outward before duplicating more files
- if content stops rendering correctly, inspect front matter, bundle type, and shortcode parameters before rewriting layouts
- if production output diverges from local preview, compare base URL, environment config, and asset pipeline assumptions first
