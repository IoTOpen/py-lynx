from typing import Optional

from src.lynx import Filter, User, OKResponse, MetaObject
from src.lynx.api_client import APIClient
from src.lynx.controller import Controller


class UserController(Controller):
    def __init__(self, api_client: APIClient):
        super().__init__(api_client)

    def get_users(self, filter: Optional[Filter] = None):
        path = "api/v2/user{0}".format(self.format_query_string(filter))
        resp = self._api_client.request("GET", path)
        res = []
        for x in resp:
            res.append(User(**x))
        return res

    def get_user(self, id: int):
        path = "api/v2/user/{0}".format(id)
        resp = self._api_client.request("GET", path)
        return User(**resp)

    def create_user(self, user: User):
        path = "api/v2/user"
        resp = self._api_client.request("POST", path, json=user.to_dict())
        return User(**resp)

    def update_user(self, user: User):
        path = "api/v2/user/{0}".format(user.id)
        resp = self._api_client.request("PUT", path, json=user.to_dict())
        return User(**resp)

    def delete_user(self, user: User):
        path = "api/v2/user/{0}".format(user.id)
        resp = self._api_client.request("DELETE", path)
        return OKResponse(**resp)

    def get_user_meta(self, id: int, key: str):
        path = "api/v2/user/{0}/meta/{1}".format(id, key)
        resp = self._api_client.request("GET", path)
        return MetaObject(**resp)

    def create_user_meta(self, id: int, key: str, meta: MetaObject, silent: Optional[bool] = False):
        qs = self.format_query_string(dict({"silent": silent}))
        path = "api/v2/user/{0}/meta/{1}{2}".format(id, key, qs)
        resp = self._api_client.request("POST", path, json=meta.to_dict())
        return MetaObject(**resp)

    def update_user_meta(self, id: int, key: str, meta: MetaObject, silent: Optional[bool] = False,
                         create_missing: Optional[bool] = False):
        qs = self.format_query_string(dict({"silent": silent, "create_missing": create_missing}))
        path = "api/v2/user/{0}/meta/{1}{2}".format(id, key, qs)
        resp = self._api_client.request("PUT", path, json=meta.to_dict())
        return MetaObject(**resp)

    def delete_user_meta(self, id: int, key: str, silent: Optional[bool] = False):
        qs = self.format_query_string(dict({"silent": silent}))
        path = "api/v2/user/{0}/meta/{1}{2}".format(id, key, qs)
        resp = self._api_client.request("DELETE", path)
        return OKResponse(**resp)

    def get_me(self):
        path = "api/v2/user/me"
        resp = self._api_client.request("GET", path)
        return User(**resp)

    def update_me(self, user: User):
        path = "api/v2/user/me"
        resp = self._api_client.request("PUT", path, json=user.to_dict())
        return User(**resp)
