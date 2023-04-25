from fastapi import FastAPI, HTTPException
from pydantic import ValidationError
from src.schemas import Product
from src.crud import (
    write_product,
    read_products,
    uptodate_product,
    delete_product,
    get_product_by_id,
    sort_products_by_price,
    truncate_db
)
from src.product_validator import validate

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Welcome to Emperia."}


@app.get("/product/{product_id}")
def get_product(product_id):
    """
    The get_product endpoint retrieves a product by its ID.
    Args:
        product_id (int): The ID of the product to retrieve.
    Returns:
        dict: A dictionary containing the product information.
    Raises:
        HTTPException: If the product is not found.
    """
    product = get_product_by_id(product_id) if get_product_by_id(product_id) else None
    if product:
        return product
    else:
        raise HTTPException(status_code=404, detail="Product not found.")


@app.post("/product/all")
def get_products():
    """
    The get_products endpoint retrieves all the products.
    Returns:
        list: A list of dictionaries containing the product information.
    Raises:
        HTTPException: If there are no products available.
    """
    products = read_products()
    if products:
        return products
    else:
        raise HTTPException(status_code=404, detail="No products available.")


@app.post("/product/add")
def add_product(product: Product):
    """
    The add_product endpoint adds a new product to the database.
    Args:
        product (Product): A Pydantic model representing the new product.
    Returns:
        dict: A dictionary containing a message indicating that the product was added successfully.
    Raises:
        HTTPException: If the new product is invalid or if the product already exists.
    """
    try:
        validate(product)
    except ValidationError as e:
        raise HTTPException(status_code=422, detail=str(e))

    products = read_products()
    if product in products:
        raise HTTPException(status_code=409, detail="The product already exists.")

    write_product(product)
    return {"message": "Product added successfully."}


@app.put("/product/update/{product_id}")
def update_product(product: Product, product_id):
    """
    The update_product endpoint updates an existing product in the database.
    Args:
        product (Product): A Pydantic model representing the updated product.
        product_id (int): The ID of the product to update.
    Returns:
        dict: A dictionary containing a message indicating that the product was updated successfully.
    Raises:
        HTTPException: If the product is not found.
    """
    product_flag = get_product_by_id(product_id) if get_product_by_id(product_id) else None
    if product_flag:
        uptodate_product(product_id, product.name, product.description, product.price)
        return {"message": "Product updated successfully."}
    else:
        raise HTTPException(status_code=404, detail="Product not found.")


@app.get("/product/all/sorted")
def sort_products():
    """GET endpoint to retrieve all products sorted by price.
    Returns:
        List[Product]: List of all products sorted by price.
    Raises:
        HTTPException: If there are no products available in the database.
    """
    products = sort_products_by_price()
    if products:
        return products
    else:
        raise HTTPException(status_code=404, detail="No products available.")


@app.delete("/product/remove/{product_id}")
def remove_product(product_id: int):
    """DELETE endpoint to remove a product by ID.
    Args:
        product_id (int): ID of the product to remove.
    Returns:
        Dict[str, str]: Message indicating successful product removal.
    Raises:
        HTTPException: If the product to remove does not exist in the database.
    """
    product = get_product_by_id(product_id) if get_product_by_id(product_id) else None
    if product:
        delete_product(product_id)
        return {"message": "Product removed successfully."}
    else:
        raise HTTPException(status_code=404, detail="Product not found.")


@app.delete("/product/flush")
def flush_db():
    """DELETE endpoint to delete all products from the database.
    Returns:
        Dict[str, str]: Message indicating successful database truncation.
    Raises:
        HTTPException: If there are no products in the database.
    """
    if read_products():
        truncate_db()
        return {"message": " Database is empty"}
    else:
        raise HTTPException(status_code=404, detail="No product is found.")
