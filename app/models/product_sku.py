from sqlalchemy import UUID, Column, Integer, String

from app.db.base import Base


class product_sku(Base):
    __tablename__ = "product_skus"

    id = Column(UUID, primary_key=True)
    sku = Column(String(50), nullable=False, unique=True)
    quantity = Column(Integer, nullable=False)
    product_id = Column
