from pathlib import Path

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    BASE_DIR: Path = Path(__file__).absolute().parent.parent
    STATIC_DIR: Path = BASE_DIR / "statics"

    POSTGRES_USER: str = 'admin'
    POSTGRES_PASSWORD: str = 'admin'
    POSTGRES_HOST: str = 'localhost'
    POSTGRES_PORT: int = 5432
    POSTGRES_DB: str = 'postgres'
    POSTGRES_TEST_DB: str = ""
    POSTGRES_URL: str = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"  # noqa


settings = Settings()
