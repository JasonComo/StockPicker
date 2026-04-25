import yfinance as yf

class StockApiService:
    def get_price_by_ticker_symbol(self, ticker_symbol: str) -> float | None:
        try:
            ticker = yf.Ticker(ticker_symbol)
            return ticker.fast_info.last_price
        except Exception:
            return None




