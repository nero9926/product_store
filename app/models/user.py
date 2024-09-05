from datetime import datetime

from sqlalchemy import UUID, Column, Date, DateTime, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class User(Base):
    __tablename__ = "user"

    id = Column(UUID, primary_key=True)
    avatar = Column()
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)
    date_of_birth = Column(Date(), nullable=False)
    orders = relationship("Orders")
    favorites = relationship()
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now,
                        onupdate=datetime.now)
