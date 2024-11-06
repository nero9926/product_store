import logging
from pathlib import Path
from typing import Any, Mapping, Optional

from dotenv import find_dotenv, load_dotenv
from pydantic import PostgresDsn, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv(find_dotenv(".env"))


class Settings(BaseSettings):
    model_config = SettingsConfigDict(case_sensitive=True)
    BASE_DIR: Path = Path(__file__).absolute().parent.parent
    STATIC_DIR: Path = BASE_DIR / "statics"
    # POSTGRES
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str
    POSTGRES_DB: str
    PGDATA: str

    POSTGRES_TEST_DB: str = ""

    TEST_POSTGRES_URL: str = ""

    POSTGRES_URL: str = ""

    # RABBITMQ
    RABBITMQ_USER: str
    RABBITMQ_PASSWORD: str
    RABBITMQ_HOST: str
    RABBITMQ_PORT: int

    @field_validator("POSTGRES_URL", check_fields=False)
    def assemble_postgres_db_url(
        cls, v: Optional[str], values: Mapping[str, Any]
    ) -> Any:
        print(values)
        if v and isinstance(v, str):
            return v

        return str(
            PostgresDsn.build(
                scheme="postgresql+asyncpg",
                username=values.data["POSTGRES_USER"],
                password=values.data["POSTGRES_PASSWORD"],
                host=values.data["POSTGRES_HOST"],
                port=int(values.data["POSTGRES_PORT"]),
                path=f'/{values.data["POSTGRES_DB"]}',
            )
        )

    # @field_validator("TEST_POSTGRES_URL", check_fields=False)
    # def assemble_test_postgres_url(
    #     cls, v: Optional[str], values: Mapping[str, Any]
    # ) -> Any:
    #     print(values)
    #     if not values.data.get("POSTGRES_TEST_DB"):
    #         return ""
    #     if v and isinstance(v, str):
    #         return v

    #     return str(
    #         PostgresDsn.build(
    #             scheme="postgresql",
    #             username=values.data["POSTGRES_USER"],
    #             # password=values.data["POSTGRES_PASSWORD"],
    #             password="admin",
    #             # host=values.data["POSTGRES_HOST"],
    #             host="localhost",
    #             # port=int(values.data["POSTGRES_PORT"]),
    #             port=5433,
    #             path=f'{values.data["POSTGRES_TEST_DB"]}',
    #         )
    #     )


settings = Settings()

logging.basicConfig(
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)
