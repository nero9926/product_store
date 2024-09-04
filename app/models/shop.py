from datetime import datetime

from sqlalchemy import UUID, Column, Date, DateTime, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Shop(Base):
    __tablename__ = "shops"

    id = Column(UUID, primary_key=True)
    name = Column(String(50), nullable=False)
    owner = Column(String(50), nullable=False)
    products = Column()
