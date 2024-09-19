from pydantic import Field

from app.schemas import BaseSchema


class CategoryOut(BaseSchema):
    id: int
    name: str


class CategoryIn(BaseSchema):
    name: str = Field(default="name")
