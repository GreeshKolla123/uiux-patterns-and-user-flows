from fastapi import FastAPI
from dotenv import load_dotenv
from app.routers import products, cart, checkout, register, login

load_dotenv()
app = FastAPI()

app.include_router(products.router)
app.include_router(cart.router)
app.include_router(checkout.router)
app.include_router(register.router)
app.include_router(login.router)