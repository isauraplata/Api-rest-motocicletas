from sqlalchemy.orm import Session
from models.motorcycle import Motorcycle
from schemas.motorcycle import MotorcycleCreate

class MotorcycleRepository:
    @staticmethod
    def create(db: Session, motorcycle: MotorcycleCreate):
        db_motorcycle = Motorcycle(**motorcycle.dict())
        db.add(db_motorcycle)
        db.commit()
        db.refresh(db_motorcycle)
        return db_motorcycle
    
    @staticmethod
    def get_by_id(db: Session, motorcycle_id: int):
        return db.query(Motorcycle).filter(Motorcycle.id == motorcycle_id).first()
    
    @staticmethod
    def get_by_license_plate(db: Session, license_plate: str):
        return db.query(Motorcycle).filter(Motorcycle.license_plate == license_plate).first()
    
    @staticmethod
    def get_all(db: Session, skip: int = 0, limit: int = 100):
        return db.query(Motorcycle).offset(skip).limit(limit).all()
    
    @staticmethod
    def get_by_customer(db: Session, customer_id: int):
        return db.query(Motorcycle).filter(Motorcycle.customer_id == customer_id).all()
    
    @staticmethod
    def update(db: Session, motorcycle_id: int, motorcycle_data):
        db_motorcycle = MotorcycleRepository.get_by_id(db, motorcycle_id)
        if db_motorcycle:
            for key, value in motorcycle_data.dict(exclude_unset=True).items():
                setattr(db_motorcycle, key, value)
            db.commit()
            db.refresh(db_motorcycle)
        return db_motorcycle
    
    @staticmethod
    def delete(db: Session, motorcycle_id: int):
        db_motorcycle = MotorcycleRepository.get_by_id(db, motorcycle_id)
        if db_motorcycle:
            db.delete(db_motorcycle)
            db.commit()
            return True
        return False