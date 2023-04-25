from pydantic import BaseModel
from typing import Optional, List

# Defining a Pydantic BaseModel class named "Product"
class Product(BaseModel):
    id: Optional[int] = None
    name: str
    description: str
    price: float
