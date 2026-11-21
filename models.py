
from sqlalchemy import Column, Integer, String
from database import Base


class Student(Base):

    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    usn = Column(String(20), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    branch = Column(String(100), nullable=False)
