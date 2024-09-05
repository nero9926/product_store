from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    products = relationship("Product_Category", backref="category")

    def __repr__(self) -> str:
        return f"{self.id} {self.name}"
