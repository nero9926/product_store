from typing import List

from pydantic import UUID4, Field

from app.models.product import Product
from app.schemas import BaseSchema


class ShopOut(BaseSchema):
    id: UUID4
    name: str
    owner: UUID4
    # products: List[UUID4]


class ShopIn(BaseSchema):
    name: str = Field()
    owner: UUID4 = Field()
