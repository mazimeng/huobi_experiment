import os

from huobi.client.market import MarketClient

api_key = os.environ.get("API_KEY")
secret_key = os.environ.get("SECRET_KEY")
market_client = MarketClient(api_key=api_key,
                             secret_key=secret_key)
obj = market_client.get_market_detail("btcusdt")
obj.print_object()
