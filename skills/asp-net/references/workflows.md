# ASP.NET workflows

## Establish the target

- confirm .NET and ASP.NET Core version
- confirm Minimal APIs, MVC, Razor Pages, or hybrid posture
- confirm hosting and deployment model
- confirm data-access and background-work posture

## Day-two workflow

- start from the composition root and public contracts
- keep config and service registration explicit
- separate transport, application logic, and infrastructure
- verify build, tests, and startup after changes

## Common commands

```bash
dotnet build
dotnet test
dotnet run
```

```bash
dotnet watch run
dotnet ef database update
```

## Verification

- run `dotnet build`, `dotnet test`, and a local startup path such as `dotnet run` after changing hosting, endpoints, or DI wiring
- confirm middleware order, endpoint contracts, typed options, and health or logging behavior still match the deployment model
- verify persistence and background-work registration from the composition root instead of assuming service lifetimes remained valid

## Troubleshooting and recovery

- if startup fails after refactors, compare service registration, options binding, and environment-specific config before touching domain code
- if request behavior drifts, inspect middleware order and endpoint filters before broad controller or handler rewrites
- if EF Core or jobs become fragile, isolate infrastructure changes behind a focused test harness and reintroduce them incrementally
