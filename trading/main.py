from datetime import datetime
from enum import Enum
from typing import List, Optional
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(
    title="Trading App"
)

fake_users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
    {"id": 3, "name": "Charlie", "email": "charlie@example.com"},
    {"id": 4, "name": "David", "email": "david@example.com"},
    {"id": 5, "name": "Eve", "email": "eve@example.com", "degree": [
        {"id": 1, "created_at": "2024-01-01T00:00:00", "type_degree": "expert"}
    ]},
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

class DegreeType(Enum):
    newbie = "newbie"
    expert = "expert"

class Degree(BaseModel):
    id: int
    created_at: datetime
    type_degree: DegreeType

class Trade(BaseModel):
    id: int
    user_id: int
    currency: str = Field(min_length=3)
    side: str
    price: float = Field(ge=0)
    amount: float


class User(BaseModel):
    id: int
    name: str 
    email: str 
    degree: Optional[List[Degree]] = []

@app.get("/users/{user_id}", response_model=List[User])
def get_user(user_id: int):
    return [user for user in fake_users if user.get("id") == user_id]




@app.post("/trades")
def add_trades(trades: List[Trade]):
    fake_trades.extend(trades)
    return {"status": 200, "data": fake_trades}