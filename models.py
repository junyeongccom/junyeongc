from sqlalchemy import Column, Integer, String
from database import Base

class Member(Base):
    __tablename__ = "members"

    user_id = Column(Integer, primary_key=True, index=True) 
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False) 

