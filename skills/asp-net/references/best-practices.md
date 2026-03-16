# ASP.NET best practices

## Scope

- confirm .NET and ASP.NET Core version
- confirm Minimal APIs, MVC, Razor Pages, or hybrid posture
- confirm hosting and deployment model
- confirm data-access and background-work posture

## Default design choices

- Use constructor injection and explicit lifetimes.
- Keep endpoint handlers thin and push workflows into services or application layers.
- Use typed options or equivalent bound configuration.
- Make middleware order, health checks, and logging explicit in the host design.

## Common red flags

- controllers coordinating many persistence and infrastructure concerns
- service lifetimes chosen implicitly
- configuration values accessed everywhere
- middleware order depending on undocumented side effects

## Review checklist

- [ ] hosting style and application type are clear
- [ ] middleware, DI, and config wiring are explicit
- [ ] endpoint or controller code stays thin
- [ ] health, logging, and deployment assumptions remain visible

## Migration playbook

- stabilize hosting and config boundaries first
- add request-level tests around critical endpoints
- extract business workflows out of controllers incrementally
