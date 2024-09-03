from typing import Any, Dict

from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import as_declarative

postgres_metadata = MetaData()


@as_declarative(metadata=postgres_metadata)
class Base:
    id: Any

    def __init__(self, **kwargs: Dict) -> None:
        pass
