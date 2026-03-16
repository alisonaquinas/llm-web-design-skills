# NodeJS workflows

## Establish the target

- confirm Node.js version and module system
- confirm artifact type: service, CLI, worker, or library
- confirm deployment host
- confirm HTTP-heavy, queue-driven, or stream-processing workload

## Day-two workflow

- start from startup, transport, and resource ownership
- validate config and untrusted input at the boundary
- keep transport glue separate from core logic
- verify build, tests, and production start commands after changes

## Common commands

```bash
node --version
npm test
npm start
```

```bash
node --trace-warnings app.js
node --inspect app.js
```

## Verification

- run the package test suite, the normal start path, and one representative request or job flow through the changed code path
- confirm environment parsing, shutdown behavior, logging, and async error handling still match the operational contract
- verify package scripts and the selected module system still agree with the runtime entry point

## Troubleshooting and recovery

- if async behavior becomes hard to follow, restore one clear boundary per promise chain or request path before adding helpers
- if startup breaks, compare package scripts, module format, and environment loading before changing business logic
- if long-lived processes leak resources, inspect timers, streams, and event listeners before introducing broader concurrency changes
