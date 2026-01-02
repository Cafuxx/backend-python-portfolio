from fastapi import FastAPI, status
from models import User
import routes

api = FastAPI()

@api.post("/users", status_code=status.HTTP_201_CREATED)
def create_user(user: User):
    return routes.create_user(user)

@api.get("/users")
def list_users():
    return routes.list_users()

@api.get("/users/{user_id}")
def get_user(user_id: int):
    return routes.get_user(user_id)
