import logging
from logging.handlers import TimedRotatingFileHandler

from huobi.client.market import MarketClient
from huobi.constant import *
from huobi.exception.huobi_api_exception import HuobiApiException
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

    def callback(self, candlestick_event: 'CandlestickEvent'):
        self.logger.info(str(candlestick_event.tick))

    def error(self, e: 'HuobiApiException'):
        self.logger.error(f"{e.error_code}, {e.error_message}")

    def run(self):
        self.logger.info("started")
        market_client = MarketClient()
        market_client.sub_candlestick("btcusdt", CandlestickInterval.MIN1, self.callback, self.error)


def main():
    sub = Sub()
    sub.run()


if __name__ == '__main__':
    main()
