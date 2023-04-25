from typing import List
from bs4 import BeautifulSoup
from src.schemas import Product
from src.config import DB_PATH


def read_html_db() -> str:
    """
    Read the HTML content of the database file.
    Parameters:
        Nothing
    Returns:
        str: The HTML content of the database file.
    """
    with open(DB_PATH, "r") as f:
        content = f.read()
    return content


def write_html_db(soup: BeautifulSoup) -> None:
    """
    Write the BeautifulSoup object to the database file.
    Parameters:
        soup (BeautifulSoup): The BeautifulSoup object to write to the database file.
    Returns:
        Nothing
    """
    with open(DB_PATH, "w") as f:
        f.write(str(soup))


def generate_id(products: List[Product]) -> int:
    """
    Generate a unique ID for a new product.
    Parameters:
        products (List[Product]): The list of existing products in the database.
    Returns:
        int: A unique ID for the new product.
    """
    products_ids = [p.id for p in products]
    if products_ids:
        return max(products_ids) + 1
    else:
        return 1


def write_product(product: Product) -> None:
    """
    Add a new product to the database.
    Parameters:
        product (Product): The product to add to the database.
    Returns:
        Nothing
    """
    content = read_html_db()
    soup = BeautifulSoup(content, "html.parser")
    table = soup.find("table")
    row_data = [generate_id(read_products()), product.name, product.description, product.price]
    new_row = soup.new_tag("tr")
    for data in row_data:
        cell = soup.new_tag("td")
        cell.string = str(data)
        new_row.append(cell)
    table.append(new_row)
    write_html_db(soup)


def get_product_by_id(id: int) -> Product:
    """
    Retrieve a product from the database by ID.
    Parameters:
        id (int): The ID of the product to retrieve.
    Returns:
        Product: The product with the given ID, or None if not found.
    """
    content = read_html_db()
    soup = BeautifulSoup(content, "html.parser")
    table = soup.find("table")
    rows = table.find_all("tr")
    for row in rows:
        cells = row.find_all("td")
        if len(cells) > 0 and int(cells[0].text) == int(id):
            return Product(
                id=int(cells[0].text),
                name=cells[1].text,
                description=cells[2].text,
                price=float(cells[3].text)
            )
    return None


def read_products() -> List[Product]:
    """
    Retrieve all products from the database.
    Parameters:
        Nothing
    Returns:
        List[Product]: The list of all products in the database.
    """
    content = read_html_db()
    soup = BeautifulSoup(content, "html.parser")
    table = soup.find("table")
    products = []
    for row in table.find_all("tr")[1:]:
        cells = row.find_all("td")
        products.append(Product(
            id=int(cells[0].text),
            name=cells[1].text,
            description=cells[2].text,
            price=float(cells[3].text)
        ))
    return products


def delete_product(id: int) -> None:
    """
    Delete a product from the database by ID.
    Parameters:
        id (int): The ID of the product to delete.
    Returns:
    """
    content = read_html_db()
    soup = BeautifulSoup(content, "html.parser")
    table = soup.find("table")
    for row in table.find_all("tr"):
        cells = row.find_all("td")
        if len(cells) > 0 and int(cells[0].text) == int(id):
            row.decompose()
            break
    write_html_db(soup)
    print("Product deleted successfully!")


def truncate_db() -> None:
    """
    Delete all products from the database by ID.
    Parameters:
    Returns:
    """
    products_ids = [p.id for p in read_products()]
    if products_ids:
        for product_id in products_ids:
            delete_product(product_id)
        print("Product deleted successfully!")


def uptodate_product(id: int, name: str = None, description: str = None, price: float = None) -> None:
    """
    Update an existing product in the database with new information.
    Parameters:
        id (int): The ID of the product to be updated.
        name (str, optional): The new name of the product.
        description (str, optional): The new description of the product.
        price (float, optional): The new price of the product.
    Returns:
        None
    """
    content = read_html_db()
    soup = BeautifulSoup(content, "html.parser")
    table = soup.find("table")
    for row in table.find_all("tr"):
        cells = row.find_all("td")
        if len(cells) > 0 and int(cells[0].text) == int(id):
            if name:
                row.find_all("td")[1].string = name
            if description:
                row.find_all("td")[2].string = description
            if price:
                row.find_all("td")[3].string = str(price)
            write_html_db(soup)
            print("Product updated successfully!")


def sort_products_by_price():
    """
    Sort the products in the database by price, in descending order.
    Parameters:
        Nothing
    Returns:
        List[Product]: A list of products sorted by price, in descending order.
    """
    products = read_products()
    products.sort(key=lambda product: product.price, reverse=True)
    return products
