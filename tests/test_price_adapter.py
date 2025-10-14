# tests/test_price_adapter.py
import pytest
from src.adapters import price_adapter

def test_fetch_price_data_returns_series():
    prices = price_adapter.fetch_price_data("AAPL")
    assert prices is not None
    import pandas as pd
    assert isinstance(prices, pd.Series)

    # values should be numeric
    values = prices.values
    import numpy as np
    assert np.issubdtype(values.dtype, np.number)

def test_compute_returns_with_valid_data():
    prices = price_adapter.fetch_price_data("AAPL")
    result = price_adapter.compute_returns(prices)
    assert "20d_return" in result

    val = result["20d_return"]

    # val should be float or None
    import numbers
    assert val is None or isinstance(val, numbers.Number)


def test_compute_returns_with_insufficient_data():
    result = price_adapter.compute_returns([])
    assert result["20d_return"] is None
