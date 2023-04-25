from pydantic import ValidationError
from decimal import Decimal
from src.schemas import Product


def validate(product: Product):
    """
    this function takes a Product object as input and validates its attributes.
    Parameters:
        Product object
    Returns:
        If any of the attributes is invalid, it raises a ValidationError.
    """
    try:
        name = str(product.name)
    except ValueError:
        raise ValidationError("Product name must be a string.")

    try:
        description = str(product.description)
    except ValueError:
        raise ValidationError("Product description must be a string.")

    try:
        price = Decimal(str(product.price))
        if price <= 0:
            raise ValueError()
    except (ValueError, TypeError):
        raise ValidationError("Product price must be a positive number.")