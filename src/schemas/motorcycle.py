from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class MotorcycleBase(BaseModel):
    brand: str
    model: str
    year: int
    license_plate: str
    color: Optional[str] = None
    customer_id: int

class MotorcycleCreate(MotorcycleBase):
    pass

class MotorcycleResponse(MotorcycleBase):
    id: int
    registration_date: datetime
    
    class Config:
        orm_mode = True