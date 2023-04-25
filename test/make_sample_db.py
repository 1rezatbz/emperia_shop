import requests
import json
from src.config import check_db

# Sample data for products
sample_products = [
    {
        "id": 0,
        "name": "T-shirt",
        "description": "A comfortable and stylish cotton t-shirt",
        "price": 19.99
    },
    {
        "id": 1,
        "name": "Jeans",
        "description": "Classic denim jeans for everyday wear",
        "price": 49.99
    },
    {
        "id": 2,
        "name": "Sneakers",
        "description": "Versatile sneakers for any outfit",
        "price": 69.99
    },
    {
        "id": 3,
        "name": "Dress",
        "description": "Elegant dress for formal occasions",
        "price": 99.99
    },
    {
        "id": 4,
        "name": "Jacket",
        "description": "Stylish and warm jacket for cold weather",
        "price": 79.99
    },
    {
        "id": 5,
        "name": "Shorts",
        "description": "Comfortable shorts for summer days",
        "price": 29.99
    },
    {
        "id": 6,
        "name": "Sweater",
        "description": "Soft and cozy sweater for chilly evenings",
        "price": 59.99
    },
    {
        "id": 7,
        "name": "Skirt",
        "description": "Flattering skirt for any body type",
        "price": 39.99
    },
    {
        "id": 8,
        "name": "Blouse",
        "description": "Elegant blouse for a professional look",
        "price": 49.99
    },
    {
        "id": 9,
        "name": "Coat",
        "description": "Stylish coat for any occasion",
        "price": 89.99
    }
]


def add_product_db(data):
    url = "http://127.0.0.1:8000" + "/product/add"
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response


if __name__ == '__main__':
    check_db()
    # Add each product in the sample data to the database
    for product in sample_products:
        add_product_db(product)
    print("Data added successfully")
