from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, ForeignKey
from app.db.base import Base

class WatchList(Base):
    __tablename__ = "watch_list"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    ticker_symbol: Mapped[str] = mapped_column(String(100), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)

