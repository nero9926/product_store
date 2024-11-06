from typing import Generator

import pytest
from sqlalchemy import create_engine
from sqlalchemy.engine import Connection
from sqlalchemy_utils import create_database, database_exists, drop_database

from alembic import command
from alembic.config import Config
from app.api.deps import get_db_pg
from app.core.config import settings
from app.db.base import Base
from app.main import app
from tests.common import PGSession

# DATABASE_URL_TEST = f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}/{settings.POSTGRES_TEST_DB}"  # noqa
DATABASE_URL_TEST = f"postgresql://postgres:admin@localhost:5433/postgrestest"  # noqa


@pytest.fixture(scope="session")
def pg_connection() -> Connection:
    if database_exists(DATABASE_URL_TEST):
        drop_database(DATABASE_URL_TEST)
    create_database(DATABASE_URL_TEST)
    engine = create_engine(DATABASE_URL_TEST)
    connection = engine.connect()
    return connection


@pytest.fixture(scope="session")
def setup_pg_database(pg_connection: Connection, alembic_cfg: Config) -> Generator:  # noqa
    Base.metadata.bind = pg_connection
    alembic_cfg.config_ini_section = "postgres"
    alembic_cfg.attributes["connection"] = pg_connection

    command.upgrade(alembic_cfg, "head")

    PGSession.configure(bind=pg_connection)

    try:
        yield
    finally:
        command.downgrade(alembic_cfg, "base")


@pytest.fixture
def pg_session(pg_connection: Connection, setup_pg_database: Generator) -> Generator:  # noqa
    transaction = pg_connection.begin()
    try:
        yield PGSession()
    finally:
        transaction.rollback()
        PGSession.remove()


@pytest.fixture
def pg_db_override(pg_session: Generator) -> None:
    def get_test_db_pg() -> Generator[Generator, None, None]:
        yield pg_session

    app.dependency_overrides[get_db_pg] = get_test_db_pg


@pytest.fixture
def use_postgres(pg_db_override: Generator) -> None:
    pass
