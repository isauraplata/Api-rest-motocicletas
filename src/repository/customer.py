from sqlalchemy.orm import Session
from models.customer import Customer
from schemas.customer import CustomerCreate

class CustomerRepository:
    @staticmethod
    def create(db: Session, customer: CustomerCreate):
        db_customer = Customer(**customer.dict())
        db.add(db_customer)
        db.commit()
        db.refresh(db_customer)
        return db_customer
    
    @staticmethod
    def get_by_id(db: Session, customer_id: int):
        return db.query(Customer).filter(Customer.id == customer_id).first()
    
    @staticmethod
    def get_by_email(db: Session, email: str):
        return db.query(Customer).filter(Customer.email == email).first()
    
    @staticmethod
    def get_all(db: Session, skip: int = 0, limit: int = 100):
        return db.query(Customer).offset(skip).limit(limit).all()
    
    @staticmethod
    def update(db: Session, customer_id: int, customer_data):
        db_customer = CustomerRepository.get_by_id(db, customer_id)
        if db_customer:
            for key, value in customer_data.dict(exclude_unset=True).items():
                setattr(db_customer, key, value)
            db.commit()
            db.refresh(db_customer)
        return db_customer
    
    @staticmethod
    def delete(db: Session, customer_id: int):
        db_customer = CustomerRepository.get_by_id(db, customer_id)
        if db_customer:
            db.delete(db_customer)
            db.commit()
            return True
        return False