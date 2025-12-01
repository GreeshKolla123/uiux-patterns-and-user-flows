from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.database import SessionLocal
from app.models import Product

router = APIRouter()

@router.get("/")
def read_products():
    db = SessionLocal()
    products = db.query(Product).all()
    db.close()
    return products

@router.get("/{product_id}")
def read_product(product_id: int):
    db = SessionLocal()
    product = db.query(Product).filter(Product.product_id == product_id).first()
    db.close()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product