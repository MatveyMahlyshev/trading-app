from fastapi import FastAPI

app = FastAPI(
    title="Trading App"
)

fake_users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
    {"id": 3, "name": "Charlie", "email": "charlie@example.com"},
    {"id": 4, "name": "David", "email": "david@example.com"},
    {"id": 5, "name": "Eve", "email": "eve@example.com"}
]


fake_users2 = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
    {"id": 3, "name": "Charlie", "email": "charlie@example.com"},
    {"id": 4, "name": "David", "email": "david@example.com"},
    {"id": 5, "name": "Eve", "email": "eve@example.com"}
]

fake_trades = [
    {
        "id": 1,
        "user_id": 1,
        "currency": "USD",
        "side": "buy",
        "price": 100.50,
        "amount": 2.5
    },
    {
        "id": 2,
        "user_id": 2,
        "currency": "EUR",
        "side": "sell",
        "price": 85.75,
        "amount": 1.2
    },
    {
        "id": 3,
        "user_id": 3,
        "currency": "GBP",
        "side": "buy",
        "price": 120.00,
        "amount": 3.0
    },
    {
        "id": 4,
        "user_id": 4,
        "currency": "JPY",
        "side": "sell",
        "price": 0.90,
        "amount": 100.0
    },
    {
        "id": 5,
        "user_id": 5,
        "currency": "CAD",
        "side": "buy",
        "price": 75.25,
        "amount": 2.0
    }
]


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return [user for user in fake_users if user.get("id") == user_id]


@app.get("/trades")
def get_trades(limit: int = 1, offset: int = 1):
    return fake_trades[offset:offset + limit]

@app.post("/users/{user_id}")
def change_user_name(user_id: int, new_name: str):
    updated_user = list(filter(lambda user: user.get("id") == user_id, fake_users2))
    updated_user[0]["name"] = new_name
    return {"code": 200, "data": updated_user}

