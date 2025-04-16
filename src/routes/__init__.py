from fastapi import APIRouter
from .customer import router as customer_router
from .motorcycle import router as motorcycle_router
from .service_order import router as service_order_router

api_router = APIRouter()

api_router.include_router(customer_router, prefix="/customers", tags=["customers"])
api_router.include_router(motorcycle_router, prefix="/motorcycles", tags=["motorcycles"])
api_router.include_router(service_order_router, prefix="/service-orders", tags=["service_orders"])