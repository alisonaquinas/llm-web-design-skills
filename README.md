# llm-web-design-skills

A cross-compatible repository of 16 LLM skills for modern web design, frontend application architecture, styling systems, backend frameworks, static-site workflows, and web build tooling.

## Skill Families

### Frontend frameworks

| Skill | Description |
| --- | --- |
| `angular` | Design and review Angular apps with standalone APIs, routing, RxJS, signals, forms, and testing. |
| `nextjs` | Design and review Next.js applications with the App Router, server and client boundaries, route handlers, and deployment tradeoffs. |
| `react` | Design and review React applications with clear component boundaries, state ownership, hooks, and testable UI flows. |
| `svelte` | Design and review Svelte applications with clear reactivity, component boundaries, and SvelteKit-aware delivery patterns. |
| `vue` | Design and review Vue applications with the Composition API, single-file components, routing, and maintainable state boundaries. |

### Styling and UI systems

| Skill | Description |
| --- | --- |
| `material-design` | Apply Material Design and Material 3 principles across component libraries, theming systems, and product UX decisions. |
| `scss` | Design and review SCSS architecture, tokens, mixins, module boundaries, and maintainable stylesheet systems. |
| `tailwind` | Design and review Tailwind CSS systems with strong token discipline, component extraction rules, and maintainable utility usage. |

### Build and tooling

| Skill | Description |
| --- | --- |
| `vite` | Design and troubleshoot Vite-powered web projects, plugin chains, environment handling, and modern frontend build workflows. |

### Backend frameworks

| Skill | Description |
| --- | --- |
| `django` | Design and review Django applications with strong app boundaries, ORM discipline, forms, templates, APIs, and deployment readiness. |
| `nodejs` | Design and review Node.js services, CLIs, and runtime concerns such as modules, streams, concurrency, and operability. |
| `express-js` | Design and review Express.js APIs and web services with clear middleware, validation, routing, and operational guardrails. |
| `asp-net` | Design and review ASP.NET Core applications with clear hosting, middleware, DI, API boundaries, and operational readiness. |
| `spring-boot` | Design and review Spring Boot applications with strong configuration, layering, data boundaries, and operational guardrails. |
| `laravel` | Design and review Laravel applications with strong route, controller, validation, Eloquent, queue, and deployment boundaries. |

### Static sites and content

| Skill | Description |
| --- | --- |
| `hugo` | Design and review Hugo sites with clear content models, layouts, shortcodes, asset pipelines, and publishing workflows. |

## Installation

See [INSTALL.md](INSTALL.md) for local plugin setup and build guidance.

## Development

```bash
make lint
make test
make build
make verify
```

The Python helpers are also available directly:

```bash
python scripts/lint_skills.py
python scripts/validate_skills.py
python -m unittest discover -s tests -v
```

Build artifacts land in `built/` as one ZIP per skill. Each archive is rooted at `llm-web-design-skills/skills/<skill>/...` so release uploads match the repo layout.

## Structure

```text
llm-web-design-skills/
├── .claude-plugin/
├── .github/workflows/
├── docs/
├── linting/
├── scripts/
├── skills/
├── tests/
├── validation/
├── AGENTS.md
├── CHANGELOG.md
├── INSTALL.md
├── Makefile
└── README.md
```

## License

[MIT](LICENSE.md)
