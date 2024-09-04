from datetime import datetime

from sqlalchemy import UUID, Column, Date, DateTime, Double, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Cart(Base):
    __tablename__ = "cart"

    id = Column(UUID, primary_key=True)
    user_id = Column()
    total = Column(Double)
