from sqlalchemy import UUID, Column, ForeignKey, Integer

from app.db.base import Base


class Product_Category(Base):
    __tablename__ = 'product_category'

    id = Column(Integer(), primary_key=True)
    product_id = Column(UUID(), ForeignKey("product.id"))
    category_id = Column(Integer(), ForeignKey("category.id"))
