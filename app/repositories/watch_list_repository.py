from sqlalchemy.orm import Session
from app.models.watch_list import WatchList


class WatchListRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_watch_lists_by_user_id(self, user_id: int) -> list[WatchList]:
        return self.db.query(WatchList).filter(WatchList.user_id == user_id).all()

    def get_watch_list_by_user_id_and_ticker_symbol(self, user_id: int, ticker_symbol: str) -> WatchList | None:
        return self.db.query(WatchList).filter(WatchList.user_id == user_id, WatchList.ticker_symbol == ticker_symbol).first()

    def add_watch_list(self, watch_list: WatchList) -> WatchList:
        self.db.add(watch_list)
        self.db.commit()
        self.db.refresh(watch_list)
        return watch_list

    def delete_watch_list(self, watch_list: WatchList) -> None:
        self.db.delete(watch_list)
        self.db.commit()
