from typing import Optional

from src.lynx import Function, Filter, MetaObject, OKResponse
from src.lynx.api_client import APIClient
from src.lynx.controller import Controller


class FunctionController(Controller):
    def __init__(self, api_client: APIClient):
        super().__init__(api_client)

    def get_functions(self, installation_id: int, filter: Optional[Filter] = None):
        path = "api/v2/functionx/{0}{1}".format(installation_id, self.format_query_string(filter))
        resp = self._api_client.request("GET", path)
        res = []
        for x in resp:
            res.append(Function(**x))
        return res

    def get_function(self, installation_id: int, id: int):
        path = "api/v2/functionx/{0}/{1}".format(installation_id, id)
        resp = self._api_client.request("GET", path)
        return Function(**resp)

    def create_function(self, fun: Function):
        path = "api/v2/functionx/{0}".format(fun.installation_id)
        resp = self._api_client.request("POST", path, json=fun.to_dict())
        return Function(**resp)

    def update_function(self, fun: Function):
        path = "api/v2/functionx/{0}/{1}".format(fun.installation_id, fun.id)
        resp = self._api_client.request("PUT", path, json=fun.to_dict())
        return Function(**resp)

    def delete_function(self, fun: Function):
        path = "api/v2/functionx/{0}/{1}".format(fun.installation_id, fun.id)
        resp = self._api_client.request("DELETE", path, json=fun.to_dict())
        return OKResponse(**resp)

    def get_function_meta(self, installation_id: int, id: int, key: str):
        path = "api/v2/functionx/{0}/{1}/meta/{2}".format(installation_id, id, key)
        resp = self._api_client.request("GET", path)
        return MetaObject(**resp)

    def create_function_meta(self, installation_id: int, id: int, key: str, meta: MetaObject,
                             silent: Optional[bool] = False):
        qs = self.format_query_string(dict({"silent": silent}))
        path = "api/v2/functionx/{0}/{1}/meta/{2}{3}".format(installation_id, id, key, qs)
        resp = self._api_client.request("POST", path, json=meta.to_dict())
        return MetaObject(**resp)

    def update_function_meta(self, installation_id: int, id: int, key: str, meta: MetaObject,
                             silent: Optional[bool] = False, create_missing: Optional[bool] = False):
        qs = self.format_query_string(dict({"silent": silent, "create_missing": create_missing}))
        path = "api/v2/functionx/{0}/{1}/meta/{2}{3}".format(installation_id, id, key, qs)
        resp = self._api_client.request("PUT", path, json=meta.to_dict())
        return MetaObject(**resp)

    def delete_function_meta(self, installation_id: int, id: int, key: str, silent: Optional[bool] = False):
        qs = self.format_query_string(dict({"silent": silent}))
        path = "api/v2/functionx/{0}/{1}/meta/{2}{3}".format(installation_id, id, key, qs)
        resp = self._api_client.request("DELETE", path)
        return OKResponse(**resp)
