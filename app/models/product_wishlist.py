from sqlalchemy import UUID, Column, ForeignKey, Integer

from app.db.base import Base


class Product_Wishlist(Base):
    __tablename__ = 'product_wishlist'

    id = Column(Integer, primary_key=True)
    wishlist_id = Column(UUID, ForeignKey("wishlist.id"), primary_key=True)
    product_id = Column(UUID, ForeignKey("product.id"), primary_key=True)
