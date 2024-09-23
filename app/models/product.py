from sqlalchemy import UUID, Column, Double, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Product(Base):
    __tablename__ = "product"

    id = Column(UUID, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    description = Column(String(500), nullable=False)
    category_id = Column(Integer(), ForeignKey('category.id'))
    wishlists = relationship("Product_Wishlist", backref="product")
    price = Column(Double, nullable=False)
    shop_id = Column(UUID, ForeignKey('shop.id'))
    shop = relationship("Shop", back_populates="products")
    orders = relationship("Order_Product", backref='product')
    carts = relationship("Cart_Item", backref="product")
    sku = relationship(
        "ProductSku", backref="product", uselist=False)
