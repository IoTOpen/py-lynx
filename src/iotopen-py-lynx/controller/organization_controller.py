from typing import Optional

from src.lynx import Filter, Organization, MetaObject, OKResponse
from src.lynx.api_client import APIClient
from src.lynx.controller import Controller


class OrganizationController(Controller):
    def __init__(self, api_client: APIClient):
        super().__init__(api_client)

    def get_organizations(self, minimal: Optional[bool] = False, filter: Optional[Filter] = None):
        if not filter:
            filter = dict({})

        filter["minimal"] = minimal
        path = "api/v2/organization{0}".format(self.format_query_string(filter))
        resp = self._api_client.request("GET", path)
        res = []
        for x in resp:
            res.append(Organization(**x))
        return res

    def get_organization(self, id: int):
        path = "api/v2/organization/{0}".format(id)
        resp = self._api_client.request("GET", path)
        return Organization(**resp)

    def create_organization(self, org: Organization):
        path = "api/v2/organization"
        resp = self._api_client.request("POST", path, json=org.to_dict())
        return Organization(**resp)

    def update_organization(self, org: Organization):
        path = "api/v2/organization/{0}".format(org.id)
        resp = self._api_client.request("PUT", path, json=org.to_dict())
        return Organization(**resp)

    def delete_organization(self, org: Organization, force: Optional[bool] = False):
        qs = self.format_query_string(dict({"force": force}))
        path = "api/v2/organization/{0}{1}".format(org.id, qs)
        resp = self._api_client.request("DELETE", path)
        return OKResponse(**resp)

    def force_password_reset(self, id: int):
        path = "api/v2/organization/{0}/force_password_reset".format(id)
        resp = self._api_client.request("POST", path)
        return OKResponse(**resp)

    def get_organization_meta(self, id: int, key: str):
        path = "api/v2/organization/{0}/meta/{1}".format(id, key)
        resp = self._api_client.request("GET", path)
        return MetaObject(**resp)

    def create_organization_meta(self, id: int, key: str, meta: MetaObject, silent: Optional[bool] = False):
        qs = self.format_query_string(dict({"silent": silent}))
        path = "api/v2/organization/{0}/meta/{1}{2}".format(id, key, qs)
        resp = self._api_client.request("POST", path, json=meta.to_dict())
        return MetaObject(**resp)

    def update_organization_meta(self, id: int, key: str, meta: MetaObject, silent: Optional[bool] = False,
                                 create_missing: Optional[bool] = False):
        qs = self.format_query_string(dict({"silent": silent, "create_missing": create_missing}))
        path = "api/v2/organization/{0}/meta/{1}{2}".format(id, key, qs)
        resp = self._api_client.request("PUT", path, json=meta.to_dict())
        return MetaObject(**resp)

    def delete_organization_meta(self, id: int, key: str, silent: Optional[bool] = False):
        qs = self.format_query_string(dict({"silent": silent}))
        path = "api/v2/organization/{0}/meta/{1}{2}".format(id, key, qs)
        resp = self._api_client.request("DELETE", path)
        return OKResponse(**resp)
