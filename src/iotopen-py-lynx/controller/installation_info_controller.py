from typing import Optional

from src.lynx import InstallationInfo
from src.lynx.api_client import APIClient
from src.lynx.controller import Controller


class InstallationInfoController(Controller):
    def __init__(self, api_client: APIClient):
        super().__init__(api_client)

    def get_installation_info(self, assigned_only: Optional[bool] = False):
        path = "api/v2/installationinfo{0}".format(self.format_query_string({"assigned_only": assigned_only}))
        resp = self._api_client.request("GET", path)
        res = []
        for x in resp:
            res.append(InstallationInfo(**x))
        return res

    def get_installation_info_client_id(self, client_id: int, assigned_only: Optional[bool] = False):
        qs = self.format_query_string({"assigned_only": assigned_only})
        path = "api/v2/installationinfo/{0}{1}".format(client_id, qs)
        resp = self._api_client.request("GET", path)
        return InstallationInfo(**resp)
