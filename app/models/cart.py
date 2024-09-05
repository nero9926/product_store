from sqlalchemy import UUID, Column, Double
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Cart(Base):
    __tablename__ = "cart"

    id = Column(UUID, primary_key=True)
    user_id = relationship("User", backref='cart', uselist=False)
    total = Column(Double)
