from sqlalchemy import UUID, Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Cart_Item(Base):
    __tablename__ = "cart_item"

    id = Column(UUID, primary_key=True)
    cart_id = Column(Integer, ForeignKey('cart.id'))
    cart = relationship("Cart")
    product_id = relationship("User", backref='cart', uselist=False)
    quantity = Column(Integer, nullable=False)
