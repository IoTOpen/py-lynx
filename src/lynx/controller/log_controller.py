from datetime import datetime, timedelta
from typing import Optional

from src.lynx import LogEntry, LogPage
from src.lynx.api_client import APIClient
from src.lynx.controller import Controller


class LogController(Controller):
    def __init__(self, api_client: APIClient):
        super().__init__(api_client)

    def get_logs(self, installation_id: int, fromm: Optional[float] = None, to: Optional[float] = None,
                 limit: Optional[int] = 500, offset: Optional[int] = 0, order: Optional[str] = "desc",
                 topics: Optional[list[str]] = None):
        now = datetime.utcnow()
        if not fromm:
            fromm = (now - timedelta(days=1)).timestamp()
        if not to:
            to = now.timestamp()
        params = {
            "from": fromm,
            "to": to,
            "limit": limit,
            "offset": offset,
            "order": order
        }

        if not topics:
            topics = []
        qs = self.format_query_string(params)
        path = "api/v3beta/log/{0}{1}".format(installation_id, qs)
        resp = self._api_client.request("POST", path, json=topics)
        tmp_res = LogPage(**resp)
        data = []
        for x in tmp_res.data:
            data.append(LogEntry(**x))
        return LogPage(tmp_res.total, tmp_res.last, tmp_res.count, data)

    def get_status(self, installation_id: int, topics: Optional[list[str]] = None):
        if not topics:
            topics = []
        path = "api/v2/status/{0}".format(installation_id)
        resp = self._api_client.request("POST", path, json=topics)
        entries = []
        for x in resp:
            entries.append(LogEntry(**x))
        return entries
