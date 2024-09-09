# product_store

## Migrations

- $ alembic -n postgres revision --autogenerate -m "init"
- $ alembic -n postgres upgrade head

## Start

- $ fastapi dev app/main.py
