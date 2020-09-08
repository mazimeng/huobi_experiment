import logging
from logging.handlers import TimedRotatingFileHandler

from huobi.client.market import MarketClient
from huobi.constant import *
from huobi.exception.huobi_api_exception import HuobiApiException
from huobi.model.market import TradeDetailEvent
from huobi.model.market.candlestick_event import CandlestickEvent


def initialize_logging():
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    handler = TimedRotatingFileHandler("logs/log.log",
                                       when="d",
                                       interval=1)
    handler.setFormatter(formatter)
    logger.addHandler(handler)


class Sub(object):
    def __init__(self):
        self.logger = logging.getLogger(str(self.__class__))

    def on_bar(self, candlestick_event: 'CandlestickEvent'):
        self.logger.info(f"on_bar, {str(candlestick_event.tick.__dict__)}")

    def on_trade(self, trade_event: 'TradeDetailEvent'):
        self.logger.info(f"on_trade, {str(trade_event.__dict__)}")

    def error(self, e: 'HuobiApiException'):
        self.logger.error(f"{e.error_code}, {e.error_message}")

    def run(self):
        self.logger.info("started")
        market_client = MarketClient()
        market_client.sub_candlestick("btcusdt", CandlestickInterval.MIN1, self.on_bar, self.error)
        market_client.sub_trade_detail("btcusdt,eosusdt", self.on_trade)


def main():
    initialize_logging()
    sub = Sub()
    sub.run()


if __name__ == '__main__':
    main()
