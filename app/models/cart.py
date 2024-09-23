import uuid as uuid_pkg

from sqlalchemy import UUID, Column, Double, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Cart(Base):
    __tablename__ = "cart"

    id = Column(UUID, default=uuid_pkg.uuid4, primary_key=True)
    user_id = Column(UUID, ForeignKey('user.id'))
    user = relationship("User", backref='cart', uselist=False)
    items = relationship("Cart_Item", backref='cart')
    total = Column(Double, default=0.0, nullable=False)
