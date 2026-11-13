import http.client

from requests import request, Response


class APIClient:
    def __init__(self, base_url: str, api_key: str):
        self._base_url = base_url
        self._api_key = api_key

    def request(self, method: str, path: str, raw: bool = False, **kwargs):
        method = method.upper()
        assert method in ["GET", "DELETE", "POST", "PUT"]
        path = "{0}/{1}".format(self._base_url, path)

        headers = dict(kwargs.pop("headers", None) or {})

        headers["X-API-Key"] = self._api_key
        if "Accept" not in headers:
            headers["Accept"] = "application/json"
        # requests sets the multipart Content-Type with boundary itself
        if method in ["POST", "PUT"] and "Content-Type" not in headers and "files" not in kwargs:
            headers["Content-Type"] = "application/json; charset=utf-8"

        res = request(method, path, **kwargs, headers=headers)
        self.__check_error(res)
        if raw:
            return res.content
        return res.json()

    @staticmethod
    def __check_error(response: Response):
        if response.status_code != http.client.OK:
            if response.status_code != http.client.NOT_FOUND:
                resp = response.json()
                raise HTTPException(response.status_code, resp["message"])


class HTTPException(Exception):
    def __init__(self, status_code: int, message: str):
        msg = "Encountered an HTTP Error with status code {0}: {1}".format(status_code, message)
        self.status_code = status_code
        self.message = message
        super().__init__(msg)
