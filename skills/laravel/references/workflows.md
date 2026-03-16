# Laravel workflows

## Establish the target

- confirm Laravel and PHP version
- confirm Blade, API, Livewire, Inertia, or hybrid delivery model
- confirm database and queue posture
- confirm deployment style

## Day-two workflow

- start from the route group or capability that owns the behavior
- make validation, auth, transactions, and jobs explicit
- separate framework wiring from domain workflows
- verify migrations, tests, workers, and cache commands after changes

## Common commands

```bash
php artisan serve
php artisan test
php artisan migrate
```

```bash
php artisan queue:work
php artisan route:list
```

## Verification

- run `php artisan test`, check migrations with a safe command such as `php artisan migrate --pretend`, and exercise the affected route or job flow
- confirm validation, authorization, queue dispatch, and Eloquent writes still happen at the intended boundary
- verify config cache, route cache, and worker assumptions after deployment-oriented changes

## Troubleshooting and recovery

- if controller code expands after a change, move validation, actions, or jobs back to dedicated request, service, or job layers
- if data behavior drifts, inspect transactions, eager loading, and model events before adding more conditional controller logic
- if queue or cache behavior changes across environments, compare worker config, cache store, and deployment commands before touching feature code
