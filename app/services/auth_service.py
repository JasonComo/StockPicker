from fastapi import HTTPException
from app.schemas.user import UserCreate, Token
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.core.security import hash_password, verify_password, create_access_token


class AuthService:

    def __init__(self, repo: UserRepository):
        self.repo = repo

    def register(self, user_data: UserCreate) -> User:
        if self.repo.get_user_by_username(user_data.username):
            raise HTTPException(status_code=409, detail="Username already taken")
        if len(user_data.username) > 10:
            raise HTTPException(status_code=400, detail="Username must be 10 characters or less")
        if not 8 <= len(user_data.password) <= 12:
            raise HTTPException(status_code=400, detail="Password must be between 8 and 12 characters")
        if not any(c in "!@#$%^&*" for c in user_data.password):
            raise HTTPException(status_code=400, detail="Password must contain a symbol")

        hashed = hash_password(user_data.password)
        user = User(
            username=user_data.username,
            first_name=user_data.first_name,
            last_name=user_data.last_name,
            hashed_password=hashed
        )
        return self.repo.add_user(user)

    def login(self, username: str, password: str) -> Token:
        user = self.repo.get_user_by_username(username)
        if not user or not verify_password(password, user.hashed_password):
            raise HTTPException(status_code=401, detail="Invalid username or password")
        token = create_access_token({"sub": username})
        return Token(access_token=token, token_type="bearer")
