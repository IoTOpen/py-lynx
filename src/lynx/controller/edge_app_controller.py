from typing import Optional

from src.lynx import EdgeApp, EdgeAppVersion, EdgeAppConfig, OKResponse
from src.lynx.api_client import APIClient
from src.lynx.controller import Controller


class EdgeAppController(Controller):
    def __init__(self, api_client: APIClient):
        super().__init__(api_client)

    def get_edge_apps(self):
        path = "api/v2/edge/app"
        resp = self._api_client.request("GET", path)
        res = []
        for x in resp:
            res.append(EdgeApp(**x))
        return res

    def get_edge_apps_organization(self, organization_id: int, available: Optional[bool] = False):
        path = "api/v2/edge/app/organization/{0}{1}".format(organization_id,
                                                            self.format_query_string({"available": available}))
        resp = self._api_client.request("GET", path)
        res = []
        for x in resp:
            res.append(EdgeApp(**x))
        return res

    def get_edge_app(self, id: int):
        path = "api/v2/edge/app/{0}".format(id)
        resp = self._api_client.request("GET", path)
        return EdgeApp(**resp)

    def create_edge_app(self, app: EdgeApp):
        path = "api/v2/edge/app"
        resp = self._api_client.request("POST", path, json=app.to_dict())
        return EdgeApp(**resp)

    def update_edge_app(self, app: EdgeApp):
        path = "api/v2/edge/app/{0}".format(app.id)
        resp = self._api_client.request("PUT", path, json=app.to_dict())
        return EdgeApp(**resp)

    def delete_edge_app(self, app: EdgeApp):
        path = "api/v2/edge/app/{0}".format(app.id)
        resp = self._api_client.request("DELETE", path)
        return OKResponse(**resp)

    def download_edge_app(self, id: int, version: str):
        raise Exception("Not implemented")

    def get_edge_app_versions(self, id: int, untagged: Optional[bool] = False):
        path = "api/v2/edge/app/{0}/version{1}".format(id, self.format_query_string({"untagged": untagged}))
        resp = self._api_client.request("GET", path)
        res = []
        for x in resp:
            res.append(EdgeAppVersion(**x))
        return res

    def create_edge_app_version(self, id: int, lua: str, json: str):
        raise Exception("Not implemented")

    def name_edge_app_version(self, id: int, version: EdgeAppVersion):
        path = "api/v2/edge/app/{0}/publish}".format(id)
        resp = self._api_client.request("POST", path, json=version.to_dict())
        return EdgeAppVersion(**resp)

    def get_edge_app_config_options(self, id: int, version: str):
        path = "api/v2/edge/app/{0}/configure}".format(id, self.format_query_string({"version": version}))
        return self._api_client.request("GET", path)

    def get_edge_app_instances(self, installation_id: int):
        path = "api/v2/edge/app/configured/{0}".format(installation_id)
        resp = self._api_client.request("GET", path)
        res = []
        for x in resp:
            res.append(EdgeAppConfig(**x))
        return res

    def get_edge_app_instance(self, installation_id: int, instance_id: int):
        path = "api/v2/edge/app/configured/{0}/{1}".format(installation_id, instance_id)
        resp = self._api_client.request("GET", path)
        return EdgeAppConfig(**resp)

    def create_edge_app_instance(self, config: EdgeAppConfig):
        path = "api/v2/edge/app/configured/{0}".format(config.installation_id)
        resp = self._api_client.request("POST", path, json=config.to_dict())
        return EdgeAppConfig(**resp)

    def update_edge_app_instance(self, config: EdgeAppConfig):
        path = "api/v2/edge/app/configured/{0}/{1}".format(config.installation_id, config.id)
        resp = self._api_client.request("PUT", path, json=config.to_dict())
        return EdgeAppConfig(**resp)

    def delete_edge_app_instance(self, config: EdgeAppConfig):
        path = "api/v2/edge/app/configured/{0}/{1}".format(config.installation_id, config.id)
        resp = self._api_client.request("DELETE", path)
        return OKResponse(**resp)
