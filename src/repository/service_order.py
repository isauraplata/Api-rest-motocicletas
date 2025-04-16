from sqlalchemy.orm import Session
from models.service_order import ServiceOrder, OrderService
from schemas.service_order import ServiceOrderCreate
from config.settings import settings

class ServiceOrderRepository:
    @staticmethod
    def create(db: Session, service_order: ServiceOrderCreate):
        # Calculate subtotal, tax and total
        subtotal = sum(service.price for service in service_order.services)
        tax = subtotal * settings.TAX_RATE
        total = subtotal + tax
        
        # Create order
        db_order = ServiceOrder(
            diagnosis=service_order.diagnosis,
            mileage=service_order.mileage,
            subtotal=subtotal,
            tax=tax,
            total=total,
            status=service_order.status,
            motorcycle_id=service_order.motorcycle_id
        )
        db.add(db_order)
        db.commit()
        db.refresh(db_order)
        
        # Create services associated with the order
        for service in service_order.services:
            db_service = OrderService(
                service_order_id=db_order.id,
                name=service.name,
                price=service.price
            )
            db.add(db_service)
        
        db.commit()
        db.refresh(db_order)
        return db_order
    
    @staticmethod
    def get_by_id(db: Session, order_id: int):
        return db.query(ServiceOrder).filter(ServiceOrder.id == order_id).first()
    
    @staticmethod
    def get_all(db: Session, skip: int = 0, limit: int = 100):
        return db.query(ServiceOrder).offset(skip).limit(limit).all()
    
    @staticmethod
    def get_by_motorcycle(db: Session, motorcycle_id: int):
        return db.query(ServiceOrder).filter(
            ServiceOrder.motorcycle_id == motorcycle_id
        ).all()
    
    @staticmethod
    def update_status(db: Session, order_id: int, new_status: str):
        db_order = ServiceOrderRepository.get_by_id(db, order_id)
        if db_order:
            db_order.status = new_status
            db.commit()
            db.refresh(db_order)
        return db_order
    
    @staticmethod
    def delete(db: Session, order_id: int):
        db_order = ServiceOrderRepository.get_by_id(db, order_id)
        if db_order:
            db.delete(db_order)
            db.commit()
            return True
        return False