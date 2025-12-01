# E-commerce Platform

## Setup Instructions

1. Install dependencies: pip install -r requirements.txt
2. Create a PostgreSQL database and update .env with your database URL
3. Run the application: uvicorn app.main:app --host 0.0.0.0 --port 8000

## API Endpoints

### User Authentication

* POST /auth/register: Register a new user
* POST /auth/login: Login an existing user

### Product Catalog

* GET /products: List all products
* GET /products/{product_id}: Get a product by ID

### Shopping Cart

* POST /cart/add: Add a product to the cart
* GET /cart: Get the cart contents

### Order Management

* POST /orders: Create a new order