# from typing import List, Optional

from pydantic import UUID4

from app.schemas import BaseSchema


class ProductSkuOut(BaseSchema):
    id: UUID4
    sku: str
    quantity: int


# class ProductIn(BaseSchema):
#     name: str = Field()
#     description: str = Field(default=None)
#     category_id: int = Field(default=None)
#     # wishlists: str = Field(default=None)
#     price: float = Field()
#     shop_id: UUID4 = Field(default=None)
#     # orders: str = Field(default=None)
#     # sku: str = Field()
