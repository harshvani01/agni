"""
Price Adapter:
Fetch stock price data (historical + latest) using yfinance.
Will compute basic price-based signals like returns.
"""

import yfinance as yf
import logging

logger = logging.getLogger(__name__)

def fetch_price_data(ticker: str):
    try:
        df = yf.download(
            ticker,
            period="60d",
            interval="1d",
            progress=False,
            auto_adjust=True  # adjusted close is now in "Close"
        )

        if "Close" not in df.columns:
            raise ValueError(f"No 'Close' price found for ticker {ticker}")

        return df["Close"]

    except Exception as e:
        logger.error(f"Failed to fetch prices for {ticker}: {e}")
        return None

def compute_returns(prices):
    if prices is None or len(prices) < 20:
        return {"20d_return": None}

    try:
        past_price = prices.iloc[-20]
        latest_price = prices.iloc[-1]
        return {"20d_return": (latest_price - past_price) / past_price}
    except Exception as e:
        logger.error(f"Failed to compute returns: {e}")
        return {"20d_return": None}

