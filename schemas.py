
from pydantic import BaseModel, EmailStr, ConfigDict, Field


class StudentCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    usn: str = Field(min_length=3, max_length=20)
    email: EmailStr
    branch: str = Field(min_length=2, max_length=100)


class StudentResponse(StudentCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)
