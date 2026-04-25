from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.repositories.user_repository import UserRepository
from app.repositories.watch_list_repository import WatchListRepository
from app.services.user_service import UserService
from app.services.watch_list_service import WatchListService
from app.services.auth_service import AuthService
from app.services.stock_api_service import StockApiService


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_user_repo(db: Session = Depends(get_db)) -> UserRepository:
    return UserRepository(db)


def get_watch_list_repo(db: Session = Depends(get_db)) -> WatchListRepository:
    return WatchListRepository(db)


def get_stock_api_service() -> StockApiService:
    return StockApiService()


def get_user_service(repo: UserRepository = Depends(get_user_repo)) -> UserService:
    return UserService(repo)


def get_auth_service(repo: UserRepository = Depends(get_user_repo)) -> AuthService:
    return AuthService(repo)


def get_watch_list_service(
    repo: WatchListRepository = Depends(get_watch_list_repo),
    stock_api: StockApiService = Depends(get_stock_api_service)
) -> WatchListService:
    return WatchListService(repo, stock_api)
