import uuid as uuid_pkg

from sqlalchemy import UUID, Column, ForeignKey, Integer, String

from app.db.base import Base


class ProductSku(Base):
    __tablename__ = "productsku"

    id = Column(UUID, default=uuid_pkg.uuid4, primary_key=True)
    sku = Column(String(50), nullable=False, unique=True)
    quantity = Column(Integer, nullable=False)
    product_id = Column(UUID, ForeignKey("product.id"))
