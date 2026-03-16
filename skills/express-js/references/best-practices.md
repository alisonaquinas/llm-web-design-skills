# Express.js best practices

## Scope

- confirm Express and Node versions
- confirm API-only or mixed web-app scope
- confirm auth and session posture
- confirm deployment and reverse-proxy model

## Default design choices

- Use routers to organize capabilities and keep route modules small.
- Use schema validation at request boundaries for params, query, headers, and bodies.
- Centralize error handling and response shaping.
- Make logging, correlation, and trusted-proxy behavior explicit.

## Common red flags

- middleware stacks with fragile ordering assumptions
- route files coordinating persistence and business logic directly
- validation deferred to downstream libraries
- security-sensitive proxy or cookie settings left implicit

## Review checklist

- [ ] deployment model and auth posture are clear
- [ ] middleware ordering is explicit and justified
- [ ] validation and errors are handled consistently
- [ ] domain logic is not trapped inside route handlers

## Migration playbook

- stabilize validation and error handling first
- split oversized route files by capability
- extract business workflows into services incrementally
