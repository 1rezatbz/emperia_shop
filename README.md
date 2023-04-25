# simple E-Commerce Shop 

This API allows users to browse and manage products in a catalog.

## Getting Started

### Prerequisites

- Python 3.9
- Pipenv

### Installing

1. Clone this repository: `git clone https://github.com/your-username/product-catalog-api.git`
2. Install dependencies: `pipenv install`
3. Start the server: `pipenv run uvicorn main:app --reload`

## API Endpoints

### `GET /products`

Retrieves a list of all products in the catalog.

### `POST /products`

Adds a new product to the catalog.

### `GET /products/{product_id}`

Retrieves a specific product from the catalog.

### `PUT /products/{product_id}`

Updates an existing product in the catalog.

### `DELETE /products/{product_id}`

Deletes a product from the catalog.

## Data Model

### Product

A product in the catalog.

| Field       | Type    | Description              |
| ----------- | ------- | ------------------------ |
| `id`        | integer | The unique identifier.   |
| `name`      | string  | The name of the product. |
| `price`     | float   | The price of the product.|
| `quantity`  | integer | The quantity available.  |

## Built With

- FastAPI - Python web framework
- Pydantic - Data validation and serialization library
- Requests - HTTP library
- Beautiful Soup - HTML parsing library

