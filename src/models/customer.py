from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database.session import Base

class Customer(Base):
    __tablename__ = "customers"
    
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, index=True, nullable=False)
    phone = Column(String(20))
    address = Column(String(255))
    registration_date = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    motorcycles = relationship("Motorcycle", back_populates="customer", cascade="all, delete-orphan")