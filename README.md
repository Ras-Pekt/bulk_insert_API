# Bulk Insert API

A Django API for bulk inserting products and their variants.

## Features

- Bulk create products and their variants using a single API endpoint
- Uses Django Rest Framework for API functionality
- Supports JSON serialization and deserialization of product data

## Installation

1. Clone the repository: `git clone https://github.com/Ras-Pekt/bulk_insert_API.git`
2. Install dependencies: `pip install -r requirements.txt`
3. CD into the project directory: `cd bulk_insert_api`
4. Run migrations: `python manage.py migrate`
5. Start the server: `python manage.py runserver`

## API Endpoint

- `POST /api/`: Create a new product and its variants in bulk

## API Request Body

- `name`: Product name
- `image`: Product image URL
- `variants`: List of variant objects with `sku`, `name`, `price`, and `details` fields

## Example API Request

### Using cURL

```bash
curl -X POST \
  http://localhost:8000/api/ \
  -H 'Content-Type: application/json' \
  -d '{
        "name": "Example Product",
        "image": "https://example.com/image.jpg",
        "variants": [
            {
                "sku": "EX-001",
                "name": "Variant 1",
                "price": 19.99,
                "details": "This is variant 1"
            },
            {
                "sku": "EX-002",
                "name": "Variant 2",
                "price": 29.99,
                "details": "This is variant 2"
            }
        ]
    }'
```

or from bulk entry from a json file

```bash
curl -X POST http://localhost:8000/api/ -H "Content-Type: application/json" -d @products.json
```

### Using Postman

1. Create a new request in Postman
2. Set the request method to `POST`
3. Set the request URL to `http://localhost:8000/api/`
4. Set the request body to `raw` and select `JSON` as the format
5. Paste the following JSON data into the request body:

```json
{
  "name": "Example Product",
  "image": "https://example.com/image.jpg",
  "variants": [
    {
      "sku": "EX-001",
      "name": "Variant 1",
      "price": 19.99,
      "details": "This is variant 1"
    },
    {
      "sku": "EX-002",
      "name": "Variant 2",
      "price": 29.99,
      "details": "This is variant 2"
    }
  ]
}
```

6. Send the request
