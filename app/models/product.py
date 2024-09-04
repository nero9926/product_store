from datetime import datetime

from sqlalchemy import UUID, Column, Date, DateTime, Double, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class User(Base):
    __tablename__ = "user"

    id = Column(UUID, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    description = Column(String(500), nullable=False)
    category_id = Column()
    price = Column(Double, nullable=False)
    shop = Column()
