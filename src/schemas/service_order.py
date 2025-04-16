from pydantic import BaseModel, validator
from typing import List, Optional
from datetime import datetime

class ServiceBase(BaseModel):
    name: str
    price: float

class ServiceOrderBase(BaseModel):
    diagnosis: str
    mileage: int
    services: List[ServiceBase]
    motorcycle_id: int
    status: Optional[str] = "Pending"

class ServiceOrderCreate(ServiceOrderBase):
    @validator('services')
    def check_services_not_empty(cls, v):
        if not v or len(v) == 0:
            raise ValueError('The service order must have at least one service')
        return v

class ServiceResponse(ServiceBase):
    id: int
    
    class Config:
        orm_mode = True

class ServiceOrderResponse(ServiceOrderBase):
    id: int
    subtotal: float
    tax: float
    total: float
    creation_date: datetime
    services: List[ServiceResponse]
    
    class Config:
        orm_mode = True