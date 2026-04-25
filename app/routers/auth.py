from fastapi import APIRouter, Depends
from app.schemas.user import UserCreate, UserResponse, Token, UserLogin
from app.services.auth_service import AuthService
from app.core.dependencies import get_auth_service

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=UserResponse)
def register(user_data: UserCreate, auth_service: AuthService = Depends(get_auth_service)):
    return auth_service.register(user_data)


@router.post("/login", response_model=Token)
def login(user_data: UserLogin, auth_service: AuthService = Depends(get_auth_service)):
    return auth_service.login(user_data.username, user_data.password)
