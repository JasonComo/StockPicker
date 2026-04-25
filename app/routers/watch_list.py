from fastapi import APIRouter, Depends
from app.schemas.watch_list import WatchListResponse, WatchListCreate
from app.services.user_service import UserService
from app.services.watch_list_service import WatchListService
from app.core.security import get_current_user
from app.core.dependencies import get_user_service, get_watch_list_service

router = APIRouter(prefix="/watchlist", tags=["watchlist"])


@router.get("/", response_model=list[WatchListResponse])
def get_watch_lists(
    watch_list_service: WatchListService = Depends(get_watch_list_service),
    user_service: UserService = Depends(get_user_service),
    username: str = Depends(get_current_user)
):
    user = user_service.get_by_username(username)
    return watch_list_service.get_watch_lists_by_user_id(user.id)


@router.post("/", response_model=WatchListResponse)
def add_watch_list(
    watch_list_data: WatchListCreate,
    watch_list_service: WatchListService = Depends(get_watch_list_service),
    user_service: UserService = Depends(get_user_service),
    username: str = Depends(get_current_user)
):
    user = user_service.get_by_username(username)
    return watch_list_service.add_watch_list(user.id, watch_list_data)


@router.delete("/{ticker_symbol}", status_code=204)
def delete_watch_list(
    ticker_symbol: str,
    watch_list_service: WatchListService = Depends(get_watch_list_service),
    user_service: UserService = Depends(get_user_service),
    username: str = Depends(get_current_user)
):
    user = user_service.get_by_username(username)
    watch_list_service.delete_watch_list(user.id, ticker_symbol)
