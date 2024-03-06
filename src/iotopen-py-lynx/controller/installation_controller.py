from typing import Optional

from src.lynx import Installation, MetaObject, OKResponse, Filter
from src.lynx.api_client import APIClient
from src.lynx.controller import Controller


class InstallationController(Controller):
    def __init__(self, api_client: APIClient):
        super().__init__(api_client)

    def get_installations(self, filter: Optional[Filter] = None):
        path = "api/v2/installation{0}".format(self.format_query_string(filter))
        resp = self._api_client.request("GET", path)
        res = []
        for x in resp:
            res.append(Installation(**x))
        return res

    def get_installation(self, installation_id: int):
        path = "api/v2/installation/{0}".format(installation_id)
        resp = self._api_client.request("GET", path)
        return Installation(**resp)

    def create_installation(self, installation: Installation):
        path = "api/v2/installation"
        resp = self._api_client.request("POST", path, json=installation.to_dict())
        return Installation(**resp)

    def update_installation(self, installation: Installation):
        path = "api/v2/installation/{0}".format(installation.id)
        resp = self._api_client.request("PUT", path, json=installation.to_dict())
        return Installation(**resp)

    def delete_installation(self, installation: Installation):
        path = "api/v2/installation/{0}".format(installation.id)
        resp = self._api_client.request("DELETE", path)
        return OKResponse(**resp)

    def get_installation_meta(self, installation_id: int, id: int, key: str):
        path = "api/v2/installation/{0}/{1}/meta/{2}".format(installation_id, id, key)
        resp = self._api_client.request("GET", path)
        return MetaObject(**resp)

    def create_installation_meta(self, installation_id: int, id: int, key: str, meta: MetaObject,
                                 silent: Optional[bool] = False):
        qs = self.format_query_string(dict({"silent": silent}))
        path = "api/v2/installation/{0}/{1}/meta/{2}{3}".format(installation_id, id, key, qs)
        resp = self._api_client.request("POST", path, json=meta.to_dict())
        return MetaObject(**resp)

    def update_installation_meta(self, installation_id: int, id: int, key: str, meta: MetaObject,
                                 silent: Optional[bool] = False, create_missing: Optional[bool] = False):
        qs = self.format_query_string(dict({"silent": silent, "create_missing": create_missing}))
        path = "api/v2/installation/{0}/{1}/meta/{2}{3}".format(installation_id, id, key, qs)
        resp = self._api_client.request("PUT", path, json=meta.to_dict())
        return MetaObject(**resp)

    def delete_installation_meta(self, installation_id: int, id: int, key: str, silent: Optional[bool] = False):
        qs = self.format_query_string(dict({"silent": silent}))
        path = "api/v2/installation/{0}/{1}/meta/{2}{3}".format(installation_id, id, key, qs)
        resp = self._api_client.request("DELETE", path)
        return OKResponse(**resp)
