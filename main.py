from fastapi import FastAPI, Path, Query
from typing import List, Optional
from pydantic import BaseModel

app = FastAPI(
title="FastAPI with Polat",
    description="Test api project",
    version="0.0.1",
    # terms_of_service="http://example.com/terms/",
    contact={
        "name": "Ali",
        # "url": "http://x-force.example.com/contact/",
        "email": "op@gmail.com",
    },
    license_info={
        "name": "SEU",
    },
)

users = []

class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]


@app.get("/users", response_model= List[User])
async def get_users():
    return users


@app.post("/users")
async def create_user(user: User):
    users.append(user)
    return "Success"

@app.get("/users/{user_id}")
async def get_user(user_id: int = Path(..., title="User ID", description="User ID", ge=0),
                   q: str = Query(None, max_length=5)):
    return {"user": users[user_id], "query": q}
