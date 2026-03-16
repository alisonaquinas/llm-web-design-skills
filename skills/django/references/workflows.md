# Django workflows

## Establish the target

- confirm Django and Python versions
- confirm template-driven, API-driven, or hybrid delivery
- confirm database backend
- confirm background-task or async posture

## Day-two workflow

- start from the business capability that owns the code
- separate settings and infrastructure wiring from domain logic
- treat migrations and permissions as high-impact design choices
- verify manage.py test, migrations, and static handling after changes

## Common commands

```bash
python manage.py runserver
python manage.py makemigrations
python manage.py migrate
```

```bash
python manage.py test
python manage.py collectstatic --noinput
```

## Verification

- run `python manage.py test`, check migrations with `python manage.py makemigrations --check`, and smoke-test the affected view, form, or API path
- confirm permissions, transactions, and validation still happen at the correct boundary instead of leaking into templates or persistence details
- verify static handling, background-task hooks, and settings behavior in the target environment after the code change

## Troubleshooting and recovery

- if migrations become risky, stage schema and data changes separately and re-test against a disposable database before proceeding
- if app ownership feels muddy, move orchestration into a service or use-case layer before splitting models or views further
- if settings or secrets drift across environments, centralize them in settings modules and remove runtime side effects from imports
