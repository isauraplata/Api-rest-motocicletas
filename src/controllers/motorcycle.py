from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from repository.motorcycle import MotorcycleRepository
from repository.customer import CustomerRepository
from schemas.motorcycle import MotorcycleCreate, MotorcycleBase

class MotorcycleController:
    @staticmethod
    def create_motorcycle(db: Session, motorcycle: MotorcycleCreate):
        # Verify customer exists
        customer = CustomerRepository.get_by_id(db, motorcycle.customer_id)
        if not customer:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Customer not found"
            )
        
        # Verify license plate is not duplicated
        db_motorcycle = MotorcycleRepository.get_by_license_plate(db, motorcycle.license_plate)
        if db_motorcycle:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="License plate already registered"
            )
        
        return MotorcycleRepository.create(db, motorcycle)
    
    @staticmethod
    def get_motorcycle(db: Session, motorcycle_id: int):
        db_motorcycle = MotorcycleRepository.get_by_id(db, motorcycle_id)
        if db_motorcycle is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Motorcycle not found"
            )
        return db_motorcycle
    
    @staticmethod
    def get_motorcycles(db: Session, skip: int = 0, limit: int = 100):
        return MotorcycleRepository.get_all(db, skip, limit)
    
    @staticmethod
    def get_motorcycles_by_customer(db: Session, customer_id: int):
        # Verify customer exists
        customer = CustomerRepository.get_by_id(db, customer_id)
        if not customer:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Customer not found"
            )
        
        return MotorcycleRepository.get_by_customer(db, customer_id)
    
    @staticmethod
    def update_motorcycle(db: Session, motorcycle_id: int, motorcycle_data: MotorcycleBase):
        db_motorcycle = MotorcycleController.get_motorcycle(db, motorcycle_id)
        
        # If license plate is being changed, verify it's not duplicated
        if motorcycle_data.license_plate != db_motorcycle.license_plate:
            existing_plate = MotorcycleRepository.get_by_license_plate(db, motorcycle_data.license_plate)
            if existing_plate:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="License plate already registered"
                )
        
        return MotorcycleRepository.update(db, motorcycle_id, motorcycle_data)
    
    @staticmethod
    def delete_motorcycle(db: Session, motorcycle_id: int):
        db_motorcycle = MotorcycleController.get_motorcycle(db, motorcycle_id)
        return MotorcycleRepository.delete(db, motorcycle_id)