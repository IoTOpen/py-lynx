from .. import OKResponse, Role
from ..api_client import APIClient
from ..controller import Controller


class RoleController(Controller):
    def __init__(self, api_client: APIClient):
        super().__init__(api_client)

    def get_roles(self):
        path = "api/v2/role"
        resp = self._api_client.request("GET", path)
        res = []
        for x in resp:
            res.append(Role(**x))
        return res

    def get_role(self, id: int):
        path = "api/v2/role/{0}".format(id)
        resp = self._api_client.request("GET", path)
        return Role(**resp)

    def create_role(self, role: Role):
        path = "api/v2/role"
        resp = self._api_client.request("POST", path, json=role.to_dict())
        return Role(**resp)

    def update_role(self, role: Role):
        path = "api/v2/role/{0}".format(role.id)
        resp = self._api_client.request("PUT", path, json=role.to_dict())
        return Role(**resp)

    def delete_role(self, role: Role):
        path = "api/v2/role/{0}".format(role.id)
        resp = self._api_client.request("DELETE", path)
        return OKResponse(**resp)

    def get_permissions(self):
        # The endpoint name is misspelled in the API
        path = "api/v2/perimission"
        return self._api_client.request("GET", path)
