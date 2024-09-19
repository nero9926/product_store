import uuid as uuid_pkg

from sqlalchemy import UUID, Column, ForeignKey, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Shop(Base):
    __tablename__ = "shop"

    id = Column(UUID, default=uuid_pkg.uuid4, primary_key=True, nullable=False)
    name = Column(String(50), nullable=False)
    owner = Column(UUID, ForeignKey("user.id"), nullable=False)
    products = relationship("Product")
