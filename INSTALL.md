# Installation

## Local development

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

Optional local linting tools for the full `make lint` path:

```bash
npm install --global markdownlint-cli2
python -m pip install yamllint ruff
```

## Build the skill archives

```bash
make build
```

## Verify build output

```bash
make verify
```

## Claude Code local plugin

```json
"llm-web-design-skills@local": true
```
