from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from repository.customer import CustomerRepository
from schemas.customer import CustomerCreate, CustomerBase

class CustomerController:
    @staticmethod
    def create_customer(db: Session, customer: CustomerCreate):
        db_customer = CustomerRepository.get_by_email(db, customer.email)
        if db_customer:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )
        return CustomerRepository.create(db, customer)
    
    @staticmethod
    def get_customer(db: Session, customer_id: int):
        db_customer = CustomerRepository.get_by_id(db, customer_id)
        if db_customer is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Customer not found"
            )
        return db_customer
    
    @staticmethod
    def get_customers(db: Session, skip: int = 0, limit: int = 100):
        return CustomerRepository.get_all(db, skip, limit)
    
    @staticmethod
    def update_customer(db: Session, customer_id: int, customer_data: CustomerBase):
        db_customer = CustomerController.get_customer(db, customer_id)
        return CustomerRepository.update(db, customer_id, customer_data)
    
    @staticmethod
    def delete_customer(db: Session, customer_id: int):
        db_customer = CustomerController.get_customer(db, customer_id)
        return CustomerRepository.delete(db, customer_id)