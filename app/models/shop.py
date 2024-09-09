from sqlalchemy import UUID, Column, ForeignKey, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Shop(Base):
    __tablename__ = "shop"

    id = Column(UUID, primary_key=True)
    name = Column(String(50), nullable=False)
    owner = Column(UUID, ForeignKey("user.id"))
    products = relationship("Product")
