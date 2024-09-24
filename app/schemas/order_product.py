from datetime import datetime
from typing import List, Optional

from pydantic import UUID4, Field

from app.schemas import BaseSchema
from app.schemas.product import ProductOutMin


class OrderProductOut(BaseSchema):
    id: UUID4
    order_id: UUID4
    product: ProductOutMin
    quantity: int


# class OrderProductIn(BaseSchema):
#     products: Optional[List[UUID4]] = Field()
