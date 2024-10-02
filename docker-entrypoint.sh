APP_UVICORN_OPTIONS="${APP_UVICORN_OPTIONS:---host 0.0.0.0 --port=8000}"

alembic -n postgres upgrade head
uvicorn ${APP_UVICORN_OPTIONS} app.main:app