from pydantic import BaseModel, EmailStr
from typing import Optional


class UserCreate(BaseModel):
    name: str
    mobile_no: Optional[str] = None
    email: EmailStr
    city: Optional[str] = None
    electricity_bill: Optional[float] = None