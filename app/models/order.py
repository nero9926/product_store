import uuid as uuid_pkg
from datetime import date, datetime, timedelta

from sqlalchemy import UUID, Column, Date, DateTime, Double, ForeignKey, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Order(Base):
    __tablename__ = "order"

    id = Column(UUID, default=uuid_pkg.uuid4, primary_key=True)
    customer_id = Column(UUID, ForeignKey('user.id'))
    total = Column(Double, nullable=False)
    date_placed = Column(DateTime(), default=datetime.now)
    deliver_date = Column(Date(), default=date.today() +
                          timedelta(days=7), nullable=False)
    status = Column(String(30), default='created')
    products = relationship("Order_Product", backref="order")
    payment_details_id = relationship(
        "PaymentDetails", backref="order", uselist=False)
