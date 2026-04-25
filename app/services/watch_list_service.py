from fastapi import HTTPException
from app.schemas.watch_list import WatchListCreate, WatchListResponse
from app.models.watch_list import WatchList
from app.repositories.watch_list_repository import WatchListRepository
from app.services.stock_api_service import StockApiService


class WatchListService:

    def __init__(self, repo: WatchListRepository, stock_api_service: StockApiService):
        self.repo = repo
        self.stock_api_service = stock_api_service

    def add_watch_list(self, user_id: int, watch_list_data: WatchListCreate) -> WatchListResponse:
        existing = self.repo.get_watch_list_by_user_id_and_ticker_symbol(user_id, watch_list_data.ticker_symbol)
        if existing:
            raise HTTPException(status_code=409, detail="Ticker already in watchlist")

        price = self.stock_api_service.get_price_by_ticker_symbol(watch_list_data.ticker_symbol)
        if price is None:
            raise HTTPException(status_code=400, detail="Invalid ticker symbol")

        watch_list = WatchList(
            user_id=user_id,
            ticker_symbol=watch_list_data.ticker_symbol
        )

        saved = self.repo.add_watch_list(watch_list)
        return WatchListResponse(
            ticker_symbol=saved.ticker_symbol,
            price=self.stock_api_service.get_price_by_ticker_symbol(saved.ticker_symbol)
        )

    def get_watch_lists_by_user_id(self, user_id: int) -> list[WatchListResponse]:
        watch_lists = self.repo.get_watch_lists_by_user_id(user_id)
        result = []
        for watch_list in watch_lists:
            result.append(WatchListResponse(
                ticker_symbol=watch_list.ticker_symbol,
                price=self.stock_api_service.get_price_by_ticker_symbol(watch_list.ticker_symbol)
            ))
        return result

    def get_watch_list_by_user_id_and_ticker_symbol(self, user_id: int, ticker_symbol: str) -> WatchList:
        watch_list = self.repo.get_watch_list_by_user_id_and_ticker_symbol(user_id, ticker_symbol)
        if not watch_list:
            raise HTTPException(status_code=404, detail="Ticker not found in watchlist")
        return watch_list

    def delete_watch_list(self, user_id: int, ticker_symbol: str) -> None:
        watch_list = self.get_watch_list_by_user_id_and_ticker_symbol(user_id, ticker_symbol)
        self.repo.delete_watch_list(watch_list)
