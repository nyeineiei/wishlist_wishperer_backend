# SQLAlchemy model. Used to define how data is stored in the database
from sqlalchemy import Column, Integer, String
from app.shared.database.base import Base

class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
