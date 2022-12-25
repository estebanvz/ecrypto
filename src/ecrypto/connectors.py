from datetime import datetime, timedelta

import pandas as pd
from binance.client import Client


class Connector:
    
    def set_configuration(self, api_key="", api_secret=""):
        pass

    def get_data(self, crypto_name, time_interval, time_in_hours):
        pass


class BinanceConnector(Connector):
    def __init__(
        self,
    ):
        self.api = "https://api.binance.com/api"

    def set_configuration(self, api_key="", api_secret=""):
        self.client = Client(api_key, api_secret)
        self.client.API_URL = self.api
    
    def get_cryptos(self, is_usdt=True):
        symbols = self.client.get_exchange_info()["symbols"]
        cryptos=[]
        for e in symbols:
            if is_usdt and not (e["quoteAsset"] in ["USDT"]):
                continue
            cryptos.append(e["symbol"])
        return cryptos
    def get_data(self, code, time_interval, time_in_hours):
        timestamp = datetime.utcnow() - timedelta(hours=time_in_hours)
        unixtime = timestamp.strftime("%Y-%m-%d %H:%M:%S")
        data = self.client.get_historical_klines(code, time_interval, unixtime)
        if len(data) == 0:
            return pd.DataFrame([])
        else:
            return pd.DataFrame(
                data,
                columns=[
                    "Open time",
                    "Open",
                    "High",
                    "Low",
                    "Close",
                    "Volume",
                    "Close time",
                    "Quote asset volume",
                    "Number of trades",
                    "Taker buy base asset volume",
                    "Taker buy quote asset volume",
                    "Ignore",
                ],
            )
