"""
Entrypoint for running the pipeline.
"""

import argparse
from adapters.price_adapter import fetch_price_data,compute_returns

def run_pipeline(ticker, config_path="config.json"):
    # TODO: Orchestrate pipeline steps
    print(compute_returns(fetch_price_data("AAPL")))
    print(f"Running pipeline for {ticker}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ticker", type=str, required=True)
    args = parser.parse_args()
    run_pipeline(args.ticker)
