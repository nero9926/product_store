from pydantic import Field, UUID4

from app.schemas import BaseSchema


class ProductCategoryOut(BaseSchema):
    id: int
    product_id: UUID4
    category_id: int


class ProductCategoryIn(BaseSchema):
    product_id: UUID4 = Field(default=None)
    category_id: int = Field(default=None)
