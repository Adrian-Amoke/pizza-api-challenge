# Pizza API Challenge

## Setup

1. Install dependencies using pipenv:
   ```bash
   pipenv install
   ```

2. Activate the virtual environment:
   ```bash
   pipenv shell
   ```

3. Set environment variables (example):
   ```bash
   export FLASK_SQLALCHEMY_DATABASE_URI="your_database_uri_here"
   ```

4. Run the Flask application:
   ```bash
   flask run --port=5555
   ```

## Database Migration & Seeding

1. Initialize migrations (only once):
   ```bash
   flask db init
   ```

2. Create a migration script after model changes:
   ```bash
   flask db migrate -m "Migration message"
   ```

3. Apply migrations to the database:
   ```bash
   flask db upgrade
   ```

4. Seed the database with initial data:
   ```bash
   python server/seed.py
   ```

## Route Summary

| Method | Endpoint                | Description                      |
|--------|-------------------------|--------------------------------|
| GET    | /pizzas                 | Get all pizzas                  |
| GET    | /restaurants            | Get all restaurants             |
| GET    | /restaurants/<id> | Get restaurant by ID            |
| DELETE | /restaurants/<id> | Delete restaurant by ID         |
| POST   | /restaurant_pizzas      | Create a restaurant pizza entry |

## Example Requests & Responses

### GET /pizzas

Request:
```bash
curl -X GET http://localhost:5555/pizzas
```

Response (200):
```json
[
  {
    "id": 1,
    "name": "Pepperoni",
    "ingredients": "cheese, pepperoni, tomato sauce"
  },
  {
    "id": 2,
    "name": "Veggie",
    "ingredients": "bell peppers, olives, mushrooms, onions"
  }
]
```

Response (404):
```json
{
  "Message": "No pizzas found"
}
```

### GET /restaurants

Request:
```bash
curl -X GET http://localhost:5555/restaurants
```

Response (200):
```json
[
  {
    "id": 1,
    "name": "Big Square",
    "address": "13 Main Street"
  },
  {
    "id": 2,
    "name": "Pizza Inn",
    "address": "14 Side Street"
  }
]
```

Response (404):
```json
{
  "Message": "No restaurants found"
}
```

### GET /restaurants/<id>

Request:
```bash
curl -X GET http://localhost:5555/restaurants/1
```

Response (200):
```json
{
  "id": 1,
  "name": "Big Square",
  "address": "13 Main Street"
}
```

Response (404):
```json
{
  "error": "Restaurant not found"
}
```

### DELETE /restaurants/<id>

Request:
```bash
curl -X DELETE http://localhost:5555/restaurants/1
```

Response (200):
```json
{
  "Message": "Restaurant deleted successfully"
}
```

Response (404):
```json
{
  "error": "Restaurant not found"
}
```

### POST /restaurant_pizzas

Request:
```bash
curl -X POST http://localhost:5555/restaurant_pizzas \\
-H "Content-Type: application/json" \\
-d '{"price": 15, "pizza_id": 1, "restaurant_id": 1}'
```

Response (201):
```json
{
  "id": 1,
  "price": 15,
  "pizza_id": 1,
  "restaurant_id": 1
}
```

Response (400):
```json
{
  "errors": ["missing required keys"]
}
```

Response (415):
```json
{
  "errors": ["Content-Type must be application/json"]
}
```

## Validation Rules

- POST /restaurant_pizzas requires JSON content type.
- Required keys: `price`, `pizza_id`, `restaurant_id`.
- Missing keys or wrong content type will return appropriate error responses.

## Postman Usage Instructions

1. Import the Postman collection file `challenge-1-pizzas.postman_collection.json` into Postman.
2. Set the environment variable `base_url` to `http://localhost:5555`.
3. Use the predefined requests to test the API endpoints.
4. Ensure the Flask server is running before sending requests.
