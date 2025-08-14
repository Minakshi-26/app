# Flask User API

A simple RESTful API built with **Python Flask** to manage users in-memory.  
Supports **CRUD operations**: Create, Read, Update, Delete.

## Endpoints
- `GET /` – Welcome message
- `GET /users` – List all users
- `GET /users/<user_id>` – Get user by ID
- `POST /users` – Create user (`{"id": "1", "name": "Alice"}`)
- `PUT /users/<user_id>` – Update user (`{"name": "NewName"}`)
- `DELETE /users/<user_id>` – Delete user

## Setup & Run
1. Install Flask:
pip install Flask

2. Run the API:
python app.py

* API runs at **[http://127.0.0.1:5001](http://127.0.0.1:5001)**


