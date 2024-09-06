from datetime import datetime

from sqlalchemy import UUID, Column, DateTime
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Wishlist(Base):
    __tablename__ = "wishlist"

    id = Column(UUID, primary_key=True)
    user_id = relationship("User", backref="wishlist", uselist=False)
    products = relationship("Product_Wishlist", backref="wishlist")
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now,
                        onupdate=datetime.now)
