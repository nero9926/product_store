from datetime import datetime
from typing import List, Optional

from pydantic import UUID4, Field

from app.schemas import BaseSchema
from app.schemas.product import ProductOutMin


class OrderProductOut(BaseSchema):
    id: int
    order_id: UUID4
    product_id: UUID4
    quantity: int


# class OrderIn(BaseSchema):
#     customer_id: UUID4 = Field()
#     products: Optional[List[UUID4]] = Field()
