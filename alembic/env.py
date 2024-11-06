import os
# import re
import sys
from logging.config import fileConfig

from alembic import context
# from app.core.config import settings
from app.db.base import *
from app.db.base import Base
from app.db.base_class import postgres_metadata
from app.db.session import postgres_engine

# from sqlalchemy import create_engine


parent_dir = os.path.abspath(os.getcwd())
sys.path.append(parent_dir)

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = postgres_metadata


def run_migrations_offline() -> None:
    connectable = config.attributes.get("connection", None)
    if connectable is None:
        connectable = postgres_engine.connect()
    context.configure(
        connection=connectable,
        target_metadata=Base.metadata,
        compare_type=True,
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    connectable = config.attributes.get("connection", None)
    if connectable is None:
        connectable = postgres_engine.connect()
    context.configure(
        connection=connectable,
        target_metadata=Base.metadata,
        compare_type=True,
    )

    with context.begin_transaction():
        context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
