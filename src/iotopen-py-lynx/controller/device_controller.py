from typing import Optional

from src.lynx import Filter, Device, MetaObject, OKResponse
from src.lynx.api_client import APIClient
from src.lynx.controller import Controller


class DeviceController(Controller):
    def __init__(self, api_client: APIClient):
        super().__init__(api_client)


    def get_devices(self, installation_id: int, filter: Optional[Filter] = None):
        path = "api/v2/devicex/{0}{1}".format(installation_id, self.format_query_string(filter))
        resp = self._api_client.request("GET", path)
        res = []
        for x in resp:
            res.append(Device(**x))
        return res

    def get_device(self, installation_id: int, id: int):
        path = "api/v2/devicex/{0}/{1}".format(installation_id, id)
        resp = self._api_client.request("GET", path)
        return Device(**resp)

    def create_device(self, dev: Device):
        path = "api/v2/devicex/{0}".format(dev.installation_id)
        resp = self._api_client.request("POST", path, json=dev.to_dict())
        return Device(**resp)

    def update_device(self, dev: Device):
        path = "api/v2/devicex/{0}/{1}".format(dev.installation_id, dev.id)
        resp = self._api_client.request("PUT", path, json=dev.to_dict())
        return Device(**resp)

    def delete_device(self, dev: Device):
        path = "api/v2/devicex/{0}/{1}".format(dev.installation_id, dev.id)
        resp = self._api_client.request("DELETE", path)
        return OKResponse(**resp)

    def get_device_meta(self, installation_id: int, id: int, key: str):
        path = "api/v2/devicex/{0}/{1}/meta/{2}".format(installation_id, id, key)
        resp = self._api_client.request("GET", path)
        return MetaObject(**resp)

    def create_device_meta(self, installation_id: int, id: int, key: str, meta: MetaObject,
                           silent: Optional[bool] = False):
        qs = self.format_query_string(dict({"silent": silent}))
        path = "api/v2/devicex/{0}/{1}/meta/{2}{3}".format(installation_id, id, key, qs)
        resp = self._api_client.request("POST", path, json=meta.to_dict())
        return MetaObject(**resp)

    def update_device_meta(self, installation_id: int, id: int, key: str, meta: MetaObject,
                           silent: Optional[bool] = False, create_missing: Optional[bool] = False):
        qs = self.format_query_string(dict({"silent": silent, "create_missing": create_missing}))
        path = "api/v2/devicex/{0}/{1}/meta/{2}{3}".format(installation_id, id, key, qs)
        resp = self._api_client.request("PUT", path, json=meta.to_dict())
        return MetaObject(**resp)

    def delete_device_meta(self, installation_id: int, id: int, key: str, silent: Optional[bool] = False):
        qs = self.format_query_string(dict({"silent": silent}))
        path = "api/v2/devicex/{0}/{1}/meta/{2}{3}".format(installation_id, id, key, qs)
        resp = self._api_client.request("DELETE", path)
        return OKResponse(**resp)
