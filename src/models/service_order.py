from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database.session import Base

class OrderService(Base):
    __tablename__ = "order_services"
    
    id = Column(Integer, primary_key=True, index=True)
    service_order_id = Column(Integer, ForeignKey("service_orders.id"), nullable=False)
    name = Column(String(100), nullable=False)
    price = Column(Float, nullable=False)
    
    # Relationship
    service_order = relationship("ServiceOrder", back_populates="services")
    
class ServiceOrder(Base):
    __tablename__ = "service_orders"
    
    id = Column(Integer, primary_key=True, index=True)
    creation_date = Column(DateTime(timezone=True), server_default=func.now())
    diagnosis = Column(Text, nullable=False)
    mileage = Column(Integer, nullable=False)
    subtotal = Column(Float, nullable=False)
    tax = Column(Float, nullable=False)
    total = Column(Float, nullable=False)
    status = Column(String(20), default="Pending")  # Pending, In Progress, Completed
    motorcycle_id = Column(Integer, ForeignKey("motorcycles.id"), nullable=False)
    
    # Relationships
    motorcycle = relationship("Motorcycle", back_populates="service_orders")
    services = relationship("OrderService", back_populates="service_order", cascade="all, delete-orphan")