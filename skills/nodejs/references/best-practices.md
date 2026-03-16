# NodeJS best practices

## Scope

- confirm Node.js version and module system
- confirm artifact type: service, CLI, worker, or library
- confirm deployment host
- confirm HTTP-heavy, queue-driven, or stream-processing workload

## Default design choices

- Prefer one module strategy per package and document any interop boundaries.
- Centralize validated config loading instead of reading process.env everywhere.
- Design long-running services with signal handling and graceful shutdown behavior defined.
- Use streams when data size or latency warrants them and keep cleanup explicit.

## Common red flags

- startup with hidden side effects on import
- unbounded async concurrency
- env reads spread through many modules
- stream processing that ignores backpressure or cleanup

## Review checklist

- [ ] module system and artifact type are clear
- [ ] startup, shutdown, and async ownership are explicit
- [ ] config and input validation live at the boundary
- [ ] operational behavior is observable and testable

## Migration playbook

- stabilize module and config boundaries first
- add tests around startup and transport edges
- introduce concurrency controls where real I/O pressure exists
