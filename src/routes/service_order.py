from fastapi import APIRouter, Depends, status, HTTPException, Response, File, UploadFile
from sqlalchemy.orm import Session
from typing import List

from database.session import get_db
from controllers.service_order import ServiceOrderController
from schemas.service_order import ServiceOrderCreate, ServiceOrderResponse, ServiceOrderUpdate

router = APIRouter()

@router.post("/", response_model=ServiceOrderResponse, status_code=status.HTTP_201_CREATED)
def create_service_order(service_order: ServiceOrderCreate, db: Session = Depends(get_db)):
    return ServiceOrderController.create_service_order(db, service_order)

@router.get("/{order_id}", response_model=ServiceOrderResponse)
def get_service_order(order_id: int, db: Session = Depends(get_db)):
    return ServiceOrderController.get_service_order(db, order_id)

@router.get("/", response_model=List[ServiceOrderResponse])
def get_service_orders(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return ServiceOrderController.get_service_orders(db, skip, limit)

@router.get("/motorcycle/{motorcycle_id}", response_model=List[ServiceOrderResponse])
def get_service_orders_by_motorcycle(motorcycle_id: int, db: Session = Depends(get_db)):
    return ServiceOrderController.get_service_orders_by_motorcycle(db, motorcycle_id)

@router.put("/{order_id}", response_model=ServiceOrderResponse)
def update_service_order(order_id: int, service_order: ServiceOrderUpdate, db: Session = Depends(get_db)):
    return ServiceOrderController.update_service_order(db, order_id, service_order)

@router.delete("/{order_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_service_order(order_id: int, db: Session = Depends(get_db)):
    result = ServiceOrderController.delete_service_order(db, order_id)
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Service order not found")
    return None

@router.get("/{order_id}/pdf", response_model=str)
def generate_service_order_pdf(order_id: int, db: Session = Depends(get_db)):
    pdf_path = ServiceOrderController.generate_pdf(db, order_id)
    return {"pdf_path": pdf_path}