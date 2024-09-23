from sqlalchemy import UUID, Column, ForeignKey, Integer

from app.db.base import Base


class Order_Product(Base):
    __tablename__ = 'order_product'

    id = Column(Integer, primary_key=True, autoincrement=True, default=1)
    order_id = Column(UUID, ForeignKey("order.id"), primary_key=True)
    product_id = Column(UUID, ForeignKey("product.id"), primary_key=True)
    quantity = Column(Integer, nullable=False)
