from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from repository.service_order import ServiceOrderRepository
from repository.motorcycle import MotorcycleRepository
from schemas.service_order import ServiceOrderCreate


class ServiceOrderController:
    @staticmethod
    def create_service_order(db: Session, service_order: ServiceOrderCreate):
        # Verify motorcycle exists
        motorcycle = MotorcycleRepository.get_by_id(db, service_order.motorcycle_id)
        if not motorcycle:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Motorcycle not found"
            )
        
        # Create the order
        return ServiceOrderRepository.create(db, service_order)
    
    @staticmethod
    def get_service_order(db: Session, order_id: int):
        db_order = ServiceOrderRepository.get_by_id(db, order_id)
        if db_order is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Service order not found"
            )
        return db_order
    
    @staticmethod
    def get_service_orders(db: Session, skip: int = 0, limit: int = 100):
        return ServiceOrderRepository.get_all(db, skip, limit)
    
    @staticmethod
    def get_service_orders_by_motorcycle(db: Session, motorcycle_id: int):
        # Verify motorcycle exists
        motorcycle = MotorcycleRepository.get_by_id(db, motorcycle_id)
        if not motorcycle:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Motorcycle not found"
            )
        
        return ServiceOrderRepository.get_by_motorcycle(db, motorcycle_id)
    
    @staticmethod
    def update_service_order_status(db: Session, order_id: int, new_status: str):
        # Verify valid statuses
        valid_statuses = ["Pending", "In Progress", "Completed"]
        if new_status not in valid_statuses:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid status. Accepted values: {', '.join(valid_statuses)}"
            )
        
        db_order = ServiceOrderController.get_service_order(db, order_id)
        return ServiceOrderRepository.update_status(db, order_id, new_status)
    
    @staticmethod
    def delete_service_order(db: Session, order_id: int):
        db_order = ServiceOrderController.get_service_order(db, order_id)
        return ServiceOrderRepository.delete(db, order_id)
    