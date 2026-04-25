from fastapi import HTTPException
from app.models.user import User
from app.repositories.user_repository import UserRepository


class UserService:

    def __init__(self, repo: UserRepository):
        self.repo = repo

    def get_by_username(self, username: str) -> User:
        user = self.repo.get_user_by_username(username)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user
