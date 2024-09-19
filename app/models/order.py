from datetime import datetime

from sqlalchemy import UUID, Column, DateTime, Double, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Order(Base):
    __tablename__ = "order"

    id = Column(UUID, primary_key=True)
    customer_id = Column(UUID, ForeignKey('user.id'))
    total = Column(Double, nullable=False)
    date_placed = Column(DateTime(), default=datetime.now)
    deliver_date = Column(DateTime(), nullable=False)
    products = relationship("Order_Product", backref="order")
    payment_details_id = relationship(
        "PaymentDetails", backref="order", uselist=False)
