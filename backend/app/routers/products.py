from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models import Product
from app.database import get_db

router = APIRouter()

@router.get('/api/products')
def get_products(db: Session = Depends(get_db)):
    return db.query(Product).all()

@router.get('/api/products/{product_id}')
def get_product(product_id: int, db: Session = Depends(get_db)):
    return db.query(Product).filter(Product.id == product_id).first()