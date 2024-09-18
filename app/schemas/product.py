from pydantic import Field

from app.schemas import BaseSchema


class ProductOut(BaseSchema):
    id: str
    name: str
    description: str
    categories: str
    wishlists: str
    price: str
    shop_id: str
    orders: str
    sku: str


class ProductIn(BaseSchema):
    name: str = Field()
    description: str = Field(default=None)
    categories: str = Field(default=None)
    wishlists: str = Field(default=None)
    price: str = Field()
    shop_id: str = Field(default=None)
    orders: str = Field(default=None)
    sku: str = Field()
