from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from app.database import get_db
from app.models import User, Product, Order, OrderItem
from app.auth import authenticate_user, create_access_token
from app.config import settings

main_router = APIRouter()

@main_router.post('/auth/register')
def register_user(user: User):
    db = next(get_db())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@main_router.post('/auth/login')
def login_user(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail='Invalid username or password')
    access_token = create_access_token(data={'sub': user.username})
    return {'access_token': access_token, 'token_type': 'bearer'}

@main_router.get('/products')
def read_products():
    db = next(get_db())
    products = db.query(Product).all()
    return products

@main_router.get('/products/{product_id}')
def read_product(product_id: int):
    db = next(get_db())
    product = db.query(Product).filter(Product.product_id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail='Product not found')
    return product

@main_router.post('/cart/add')
def add_to_cart(product_id: int, quantity: int):
    db = next(get_db())
    product = db.query(Product).filter(Product.product_id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail='Product not found')
    # add to cart logic
    return {'message': 'Product added to cart'}

@main_router.get('/cart')
def read_cart():
    db = next(get_db())
    # get cart contents logic
    return []

@main_router.post('/orders')
def create_order(shipping_address: str):
    db = next(get_db())
    # create order logic
    return {'order_id': 1, 'status': 'pending', 'total_amount': 100.0}