from typing import List, Optional

from pydantic import UUID4, Field

from app.models.shop import Shop
from app.schemas import BaseSchema


class ShopOut(BaseSchema):
    id: UUID4
    name: str
    owner: UUID4
    # products: Optional[List[UUID4]]


class ShopIn(BaseSchema):
    name: str = Field()
    owner: UUID4 = Field()
