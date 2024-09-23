from typing import List, Optional

from pydantic import UUID4, Field

from app.models.shop import Shop
from app.models.user import User
from app.schemas import BaseSchema
from app.schemas.product import ProductOut


class ShopOut(BaseSchema):
    id: UUID4
    name: str
    owner_id: UUID4
    # owner: "UserOutMin"
    products: Optional[List[ProductOut]]


class ShopOutMin(BaseSchema):
    id: UUID4
    name: str
    products: Optional[List[ProductOut]]


class ShopIn(BaseSchema):
    name: str = Field()
    owner_id: UUID4 = Field()


ShopOut.model_rebuild()
