from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.database import SessionLocal
from app.models import Order, OrderItem

router = APIRouter()

@router.post("/")
def create_order(shipping_address: str):
    db = SessionLocal()
    order = Order(user_id=1, order_date=datetime.utcnow(), total_amount=0.0, status="pending")
    db.add(order)
    db.commit()
    db.close()
    return {"order_id": order.order_id, "status": order.status, "total_amount": order.total_amount}