# product_store

## Migrations

- $ alembic -n postgres revision --autogenerate -m "init"
- $ alembic -n postgres upgrade head

## Start

- $ fastapi dev app/main.py

## Docker start

- $ docker compose up
- После запуска применить миграции, открыв новый терминал и написав команды
- $ docker exec _fast_api_container_id_ alembic -n postgres upgrade head
