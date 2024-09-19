import re
from contextlib import contextmanager
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings


def create_postgres_engine() -> Engine:

    url_tokens = {
        "POSTGRES_USER": settings.POSTGRES_USER,
        "POSTGRES_PASSWORD": settings.POSTGRES_PASSWORD,
        "POSTGRES_HOST": settings.POSTGRES_HOST,
        "POSTGRES_PORT": settings.POSTGRES_PORT,
        "POSTGRES_DB": settings.POSTGRES_DB,
    }

    POSTGRES_URL = "postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}"  # noqa
    POSTGRES_URL = re.sub(
        r"\${(.+?)}", lambda m: url_tokens[m.group(1)], POSTGRES_URL)
    print(POSTGRES_URL)
    return create_engine(POSTGRES_URL, pool_pre_ping=True)


postgres_engine = create_postgres_engine()

engines = {"postgres": postgres_engine}


SessionLocalPG = sessionmaker(
    autocommit=False, autoflush=False, bind=engines["postgres"]
)


@contextmanager
def postgres_session() -> Generator:
    session = SessionLocalPG()
    try:
        yield session
    finally:
        session.close()
