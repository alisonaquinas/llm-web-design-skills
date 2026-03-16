# Spring Boot best practices

## Scope

- confirm Spring Boot and Java version
- confirm API, MVC, messaging, or hybrid app style
- confirm data-access posture
- confirm deployment and operational model

## Default design choices

- Use typed configuration properties for grouped settings.
- Keep controllers thin and validate requests at the edge.
- Push business workflows into services or use-case-oriented application layers.
- Use Actuator deliberately and secure management endpoints for the deployment model.

## Common red flags

- controllers coordinating business workflows and transactions directly
- profiles with undocumented precedence
- entities used as public API contracts accidentally
- management endpoints exposed without review

## Review checklist

- [ ] runtime style and data posture are clear
- [ ] configuration and bean wiring are understandable
- [ ] controllers remain thin and validation happens at the edge
- [ ] operational exposure through Actuator and logging is appropriate

## Migration playbook

- stabilize configuration properties and profile behavior first
- add endpoint and persistence tests before major layering refactors
- extract business workflows out of controllers incrementally
