from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database.session import Base

class Motorcycle(Base):
    __tablename__ = "motorcycles"
    
    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String(50), nullable=False)
    model = Column(String(50), nullable=False)
    year = Column(Integer, nullable=False)
    license_plate = Column(String(20), unique=True, index=True, nullable=False)
    color = Column(String(30))
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    registration_date = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    customer = relationship("Customer", back_populates="motorcycles")
    service_orders = relationship("ServiceOrder", back_populates="motorcycle", cascade="all, delete-orphan")