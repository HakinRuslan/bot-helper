from typing import List
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import BigInteger, Text, ForeignKey, Date
from db.database.database import Base
import datetime

class User(Base):
    __tablename__ = 'users'

    telegram_id: Mapped[int] = mapped_column(BigInteger, unique=True, nullable=False)
    username: Mapped[str | None]
    name: Mapped[str | None]
    reviews: Mapped[List["Review"]] = relationship(
        "Review",
        back_populates="user",
        cascade="all, delete-orphan"
    )

    def __repr__(self): 
        return f"<User(id={self.id}, telegram_id={self.telegram_id}, username='{self.username}', username='{self.name})>"
    
class Review(Base):
    __tablename__ = 'reviews'

    type_of_item: Mapped[str | None]
    coffee: Mapped[str | None]
    desc: Mapped[str | None]
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    user: Mapped["User"] = relationship("User", back_populates="reviews")

    def __repr__(self):
        return f"<Review(id={self.id}, user_id={self.user_id}, type_of_item={self.type_of_item}, desc={self.desc}, date={self.created_at})>"