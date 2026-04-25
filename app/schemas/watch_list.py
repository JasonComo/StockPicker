from pydantic import BaseModel

class WatchListCreate(BaseModel):
    ticker_symbol: str


class WatchListResponse(BaseModel):
    ticker_symbol: str
    price: float | None
    model_config = {"from_attributes": True}



