from sqlalchemy import UUID, Column, ForeignKey, Integer, String

from app.db.base import Base


class PaymentDetails(Base):
    __tablename__ = 'paymentdetails'

    id = Column(Integer, primary_key=True)
    order_id = Column(UUID, ForeignKey("order.id"))
    status = Column(String(50), nullable=False)
    povider = Column(String(50), nullable=False)
