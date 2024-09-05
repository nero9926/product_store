from sqlalchemy import Column, ForeignKey, Integer

from app.db.base import Base


class Product_Wishlist(Base):
    __tablename__ = 'product_wishlist'

    id = Column(Integer(), primary_key=True)
    product_id = Column(Integer(), ForeignKey("products.id"))
    wishlist_id = Column(Integer(), ForeignKey("wishlist.id"))
