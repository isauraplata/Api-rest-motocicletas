from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime

class CustomerBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone: Optional[str] = None
    address: Optional[str] = None

class CustomerCreate(CustomerBase):
    pass

class CustomerResponse(CustomerBase):
    id: int
    registration_date: datetime
    
    class Config:
        orm_mode = True