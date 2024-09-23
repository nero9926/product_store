import uuid as uuid_pkg
from datetime import datetime

from sqlalchemy import UUID, Column, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Wishlist(Base):
    __tablename__ = "wishlist"

    id = Column(UUID, default=uuid_pkg.uuid4, primary_key=True)
    user_id = Column(UUID, ForeignKey('user.id'))
    products = relationship("Product_Wishlist", backref="wishlist")
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now,
                        onupdate=datetime.now)
