import urllib.parse
from typing import Optional

from src.lynx.api_client import APIClient


class Controller:
    def __init__(self, api_client: APIClient):
        self._api_client = api_client

    @staticmethod
    def format_query_string(params: Optional[dict] = None):
        if not params or len(params) == 0:
            return ""
        return "?{}".format(urllib.parse.urlencode(params, doseq=False))
