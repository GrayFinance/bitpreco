from cachetools import cached, TTLCache
import requests

class BitPreco:

    def __init__(self) -> None:
        self.url = "https://api.bitpreco.com"

    def call(self, method: str, path: str) -> dict:
        response = requests.request(method=method, url=self.url + path)
        return response.json()

    @cached(cache=TTLCache(maxsize=1, ttl=60 * 3.5))
    def get_price(self) -> dict:
        r = self.call("GET", "/btc-brl/ticker")
        return {"SELL": r["sell"], "BUY": r["buy"], "RATIO": r["var"]}
