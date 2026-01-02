from fastapi import HTTPException, status
from models import User
from database import users_db

def create_user(user: User):
    users_db.append(user)
    return user

def list_users():
    return users_db

def get_user(user_id: int):
    for user in users_db:
        if user.id == user_id:
            return user
    raise HTTPException(
        status_code=404,
        detail="User not found"
    )