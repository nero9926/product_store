from datetime import datetime

from sqlalchemy import (UUID, Column, DateTime, Double, ForeignKey, Integer,
                        String)

from app.db.base_class import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(UUID, primary_key=True)
    products = Column()
    customer_id = Column(UUID, ForeignKey('users.id'))
    total = Column(Double, nullable=False)
    date_placed = Column(DateTime(), default=datetime.now,
                         onupdate=datetime.now)
