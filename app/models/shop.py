import uuid as uuid_pkg

from sqlalchemy import UUID, Column, ForeignKey, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Shop(Base):
    __tablename__ = "shop"

    id = Column(UUID, default=uuid_pkg.uuid4, primary_key=True, nullable=False)
    name = Column(String(50), nullable=False)
    owner_id = Column(UUID, ForeignKey("user.id"), nullable=False)
    owner = relationship("User", back_populates="shops", uselist=False)
    products = relationship("Product", back_populates="shop")
