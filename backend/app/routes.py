from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.database import get_session
from app.models import Product, Order, User, OrderProduct
router = APIRouter()

class ProductRequest(BaseModel):
    name: str
    description: str
    price: float
    category: str

class OrderRequest(BaseModel):
    products: list
    shipping_address: str
    payment_method: str

class UserRequest(BaseModel):
    name: str
    email: str
    password: str

@router.get('/products')
def get_products():
    session = get_session()
    products = session.query(Product).all()
    return products

@router.post('/products')
def create_product(product: ProductRequest):
    session = get_session()
    new_product = Product(name=product.name, description=product.description, price=product.price, category=product.category)
    session.add(new_product)
    session.commit()
    return new_product

@router.get('/orders')
def get_orders():
    session = get_session()
    orders = session.query(Order).all()
    return orders

@router.post('/orders')
def create_order(order: OrderRequest):
    session = get_session()
    new_order = Order(user_id=1, status='pending', shipping_address=order.shipping_address, payment_method=order.payment_method)
    session.add(new_order)
    session.commit()
    for product in order.products:
        new_order_product = OrderProduct(order_id=new_order.id, product_id=product['id'], quantity=product['quantity'])
        session.add(new_order_product)
        session.commit()
    return new_order

@router.get('/users')
def get_users():
    session = get_session()
    users = session.query(User).all()
    return users

@router.post('/users')
def create_user(user: UserRequest):
    session = get_session()
    new_user = User(name=user.name, email=user.email, password=user.password)
    session.add(new_user)
    session.commit()
    return new_user