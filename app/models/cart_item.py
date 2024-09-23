import uuid as uuid_pkg

from sqlalchemy import UUID, Column, ForeignKey, Integer

from app.db.base_class import Base


class Cart_Item(Base):
    __tablename__ = "cart_item"

    id = Column(UUID, default=uuid_pkg.uuid4, primary_key=True)
    cart_id = Column(UUID, ForeignKey('cart.id'))
    product_id = Column(UUID, ForeignKey('product.id'))
    quantity = Column(Integer, nullable=False)
