# E-Commerce Platform Backend

## Setup Instructions

1. Clone the repository
2. Create a new virtual environment
3. Install dependencies using `pip install -r requirements.txt`
4. Create a new database using `sqlite3 app.db`
5. Run the application using `uvicorn app.main:app --host 0.0.0.0 --port 8000`

## API Endpoints

* `GET /api/products`: Retrieve a list of products
* `GET /api/products/{product_id}`: Retrieve a product by ID
* `POST /api/cart`: Add a product to the cart
* `GET /api/cart`: Retrieve the cart contents
* `POST /api/checkout`: Complete the checkout process
* `POST /api/register`: Create a new user account
* `POST /api/login`: Log in to an existing user account