from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database.session import get_db
from controllers.motorcycle import MotorcycleController
from schemas.motorcycle import MotorcycleCreate, MotorcycleResponse, MotorcycleBase

router = APIRouter()

@router.post("/", response_model=MotorcycleResponse, status_code=status.HTTP_201_CREATED)
def create_motorcycle(motorcycle: MotorcycleCreate, db: Session = Depends(get_db)):
    return MotorcycleController.create_motorcycle(db, motorcycle)

@router.get("/{motorcycle_id}", response_model=MotorcycleResponse)
def get_motorcycle(motorcycle_id: int, db: Session = Depends(get_db)):
    return MotorcycleController.get_motorcycle(db, motorcycle_id)

@router.get("/", response_model=List[MotorcycleResponse])
def get_motorcycles(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return MotorcycleController.get_motorcycles(db, skip, limit)

@router.get("/customer/{customer_id}", response_model=List[MotorcycleResponse])
def get_motorcycles_by_customer(customer_id: int, db: Session = Depends(get_db)):
    return MotorcycleController.get_motorcycles_by_customer(db, customer_id)

@router.put("/{motorcycle_id}", response_model=MotorcycleResponse)
def update_motorcycle(motorcycle_id: int, motorcycle: MotorcycleBase, db: Session = Depends(get_db)):
    return MotorcycleController.update_motorcycle(db, motorcycle_id, motorcycle)

@router.delete("/{motorcycle_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_motorcycle(motorcycle_id: int, db: Session = Depends(get_db)):
    result = MotorcycleController.delete_motorcycle(db, motorcycle_id)
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Motorcycle not found")
    return None