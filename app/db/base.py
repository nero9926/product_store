from sqlalchemy.orm import Session

from app.db.base_class import Base


def save(db: Session, data: Base):
    db.add(data)
    db.commit()
    db.refresh(data)
