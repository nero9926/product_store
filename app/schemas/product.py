from pydantic import UUID4, Field

from app.schemas import BaseSchema


class ProductOut(BaseSchema):
    id: UUID4
    name: str
    description: str
    category: int
    wishlists: str
    price: str
    shop_id: str
    orders: str
    sku: str


class ProductIn(BaseSchema):
    name: str = Field()
    description: str = Field(default=None)
    category: int = Field(default=None)
    # wishlists: str = Field(default=None)
    price: float = Field()
    shop_id: str = Field(default=None)
    # orders: str = Field(default=None)
    # sku: str = Field()
