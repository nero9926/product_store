from typing import List, Optional

from pydantic import UUID4, Field

from app.schemas import BaseSchema
from app.schemas.product_sku import ProductSkuOut


class ProductOut(BaseSchema):
    id: UUID4
    name: str
    description: str
    category_id: int
    wishlists: List
    price: float
    shop_id: UUID4
    orders: List
    sku: ProductSkuOut


class ProductOutMin(BaseSchema):
    id: UUID4
    name: str
    description: str
    category_id: int
    wishlists: List
    price: float
    shop_id: UUID4
    sku: ProductSkuOut


class ProductIn(BaseSchema):
    name: str = Field()
    description: str = Field(default=None)
    category_id: int = Field(default=None)
    price: float = Field()
    shop_id: UUID4 = Field(default=None)
