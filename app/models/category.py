from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True)
    products = relationship("Product", backref="category")

    def __repr__(self) -> str:
        return f"{self.id} {self.name}"
