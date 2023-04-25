import unittest
from src.schemas import Product
from src.config import check_db
from src.crud import (
    DB_PATH,
    read_html_db,
    write_product,
    read_products,
    uptodate_product,
    delete_product,
    get_product_by_id,
    sort_products_by_price,
    truncate_db
)


class TestCRUDFunctions(unittest.TestCase):
    db_content = 0

    def setUp(self):
        # Set up the test by reading the database and truncating it to an empty state.
        self.db_content = read_html_db()
        truncate_db()

    def tearDown(self):
        # Tear down the test by writing the original database content back to the file.
        with open(DB_PATH, "w") as f:
            f.write(self.db_content)

    def test_write_and_read_products(self):
        # Test that a product can be written to the database and then read from it.
        product = Product(id=1, name='Test Product', description='This is a test product.', price=9.99)
        write_product(product)
        products = read_products()
        self.assertIn(product, products)

    def test_get_product_by_id(self):
        # Test that a product can be retrieved from the database by its ID.
        product = Product(id=1, name='Test Product', description='This is a test product.', price=9.99)
        write_product(product)
        retrieved_product = get_product_by_id(1)
        self.assertEqual(retrieved_product, product)

    def test_update_product(self):
        # Test that a product can be updated in the database.
        product = Product(name='Test Product', description='This is a test product.', price=9.99)
        write_product(product)
        uptodate_product(id=1, name='Updated Product', price=19.99)
        updated_product = get_product_by_id(1)
        self.assertEqual(updated_product.name, 'Updated Product')
        self.assertEqual(updated_product.price, 19.99)

    def test_delete_product(self):
        # Test that a product can be deleted from the database.
        product = Product(name='Test Product', description='This is a test product.', price=9.99)
        write_product(product)
        delete_product(1)
        products = read_products()
        self.assertNotIn(product, products)

    def test_sort_products_by_price(self):
        # Test that the products can be sorted by price in descending order.
        product1 = Product(name='Test Product 1', description='This is a test product.', price=9.99)
        product2 = Product(name='Test Product 2', description='This is a test product.', price=19.99)
        product3 = Product(name='Test Product 3', description='This is a test product.', price=4.99)
        write_product(product1)
        write_product(product2)
        write_product(product3)
        sorted_products = sort_products_by_price()
        self.assertEqual(sorted_products[0].price, 19.99)
        self.assertEqual(sorted_products[1].price, 9.99)
        self.assertEqual(sorted_products[2].price, 4.99)


if __name__ == '__main__':
    check_db()
    unittest.main()
