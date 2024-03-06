from datetime import datetime, timedelta
from typing import Optional

from src.lynx import TracePage, TraceEntry
from src.lynx.api_client import APIClient
from src.lynx.controller import Controller


class TraceController(Controller):
    def __init__(self, api_client: APIClient):
        super().__init__(api_client)

    def get_traces(self, fromm: Optional[float] = None, to: Optional[float] = None, limit: Optional[int] = 1000,
                   offset: Optional[int] = 0, order: Optional[str] = "desc",
                   object_type: Optional[str] = None, object_id: Optional[str] = None,
                   id: Optional[str] = None):
        now = datetime.utcnow()
        if not fromm:
            fromm = (now - timedelta(days=1)).timestamp()
        if not to:
            to = now.timestamp()

        params = dict({
            "from": fromm,
            "to": to,
            "limit": limit,
            "offset": offset,
            "order": order
        })

        if object_type and object_id:
            params["object_id"] = object_id
            params["object_type"] = object_type
        elif id:
            params["id"] = id
        else:
            raise Exception("Either object_type/object_id or id is required")

        qs = self.format_query_string(params)
        path = "api/v2/trace{0}".format(qs)
        resp = self._api_client.request("GET", path)
        tmp_res = TracePage(**resp)
        data = []
        for x in tmp_res.data:
            data.append(TraceEntry(**x))
        return TracePage(tmp_res.total, tmp_res.last, tmp_res.count, data)
