import requests
import json
import unittest
from src.crud import (
    read_html_db,
    DB_PATH,
    truncate_db
)
BASE_URL = "http://127.0.0.1:8000"


class TestAPI(unittest.TestCase):
    db_content = 0

    def setUp(self):
        # This method is called before each test method, it reads the contents of the database
        # into memory and clears the database for testing purposes
        self.db_content = read_html_db()
        truncate_db()

    def tearDown(self):
        # This method is called after each test method, it writes the original contents of the database back to the file
        with open(DB_PATH, "w") as f:
            f.write(self.db_content)

    def test_home(self):
        # Test the home route of the API
        url = BASE_URL + "/"
        headers = {"Accept": "application/json"}
        response = requests.get(url, headers=headers)
        assert response.status_code == 200
        assert response.json() == {"message": "Welcome to Emperia."}

    def test_add_product(self):
        # Test adding a new product to the database
        url = BASE_URL + "/product/add"
        headers = {"Content-Type": "application/json", "Accept": "application/json"}
        data = {"name": "New Product", "description": "A new product", "price": 10.0}
        response = requests.post(url, headers=headers, data=json.dumps(data))
        assert response.status_code == 200
        assert response.json() == {"message": "Product added successfully."}

    def test_product(self):
        # Test getting a single product from the database
        requests.post(BASE_URL + "/product/add", headers={"Content-Type": "application/json", "Accept": "application/json"}, data=json.dumps({"name": "New Product", "description": "A new product", "price": 10.0}))
        url = BASE_URL + "/product/1"
        headers = {"Accept": "application/json"}
        response = requests.get(url, headers=headers)
        assert response.status_code == 200

    def test_get_all_products(self):
        # Test getting all products from the database
        requests.post(BASE_URL + "/product/add", headers={"Content-Type": "application/json", "Accept": "application/json"}, data=json.dumps({"name": "New Product", "description": "A new product", "price": 10.0}))
        url = BASE_URL + "/product/all"
        headers = {"Accept": "application/json"}
        response = requests.post(url, headers=headers)
        assert response.status_code == 200

    def test_update_product(self):
        # Test updating a product in the database
        requests.post(BASE_URL + "/product/add", headers={"Content-Type": "application/json", "Accept": "application/json"}, data=json.dumps({"name": "New Product", "description": "A new product", "price": 10.0}))
        headers = {"Content-Type": "application/json", "Accept": "application/json"}
        url = BASE_URL + "/product/update/1"
        data = {"id": 1, "name": "Updated Product", "description": "An updated product", "price": 15.0}
        response = requests.put(url, headers=headers, data=json.dumps(data))
        assert response.status_code == 200
        assert response.json() == {"message": "Product updated successfully."}

    def test_remove_product(self):
        # Test removing a product from the database
        requests.post(BASE_URL + "/product/add", headers={"Content-Type": "application/json", "Accept": "application/json"}, data=json.dumps({"name": "New Product", "description": "A new product", "price": 10.0}))
        url = BASE_URL + "/product/remove/1"
        headers = {"Accept": "application/json"}
        response = requests.delete(url, headers=headers)
        assert response.status_code == 200
        assert response.json() == {"message": "Product removed successfully."}


if __name__ == '__main__':
    unittest.main()
