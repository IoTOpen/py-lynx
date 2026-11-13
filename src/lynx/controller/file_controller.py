import os

from .. import File, OKResponse
from ..api_client import APIClient
from ..controller import Controller


class FileController(Controller):
    def __init__(self, api_client: APIClient):
        super().__init__(api_client)

    def get_files_installation(self, installation_id: int):
        path = "api/v2/file/installation/{0}".format(installation_id)
        resp = self._api_client.request("GET", path)
        res = []
        for x in resp:
            res.append(File(**x))
        return res

    def get_file_installation(self, installation_id: int, file_id: int):
        path = "api/v2/file/installation/{0}/{1}".format(installation_id, file_id)
        resp = self._api_client.request("GET", path)
        return File(**resp)

    def get_files_organization(self, organization_id: int):
        path = "api/v2/file/organization/{0}".format(organization_id)
        resp = self._api_client.request("GET", path)
        res = []
        for x in resp:
            res.append(File(**x))
        return res

    def get_file_organization(self, organization_id: int, file_id: int):
        path = "api/v2/file/organization/{0}/{1}".format(organization_id, file_id)
        resp = self._api_client.request("GET", path)
        return File(**resp)

    def create_file_installation(self, installation_id: int, file_name: str, mime: str, file):
        path = "api/v2/file/installation/{0}".format(installation_id)
        resp = self._api_client.request("POST", path, files=self.__multipart(file_name, mime, file))
        return File(**resp[0])

    def create_file_organization(self, organization_id: int, file_name: str, mime: str, file):
        path = "api/v2/file/organization/{0}".format(organization_id)
        resp = self._api_client.request("POST", path, files=self.__multipart(file_name, mime, file))
        return File(**resp[0])

    def update_file_installation(self, installation_id: int, file_id: int, file_name: str, mime: str, file):
        path = "api/v2/file/installation/{0}/{1}".format(installation_id, file_id)
        resp = self._api_client.request("PUT", path, files=self.__multipart(file_name, mime, file))
        return File(**resp)

    def update_file_organization(self, organization_id: int, file_id: int, file_name: str, mime: str, file):
        path = "api/v2/file/organization/{0}/{1}".format(organization_id, file_id)
        resp = self._api_client.request("PUT", path, files=self.__multipart(file_name, mime, file))
        return File(**resp)

    def delete_file_installation(self, installation_id: int, file_id: int):
        path = "api/v2/file/installation/{0}/{1}".format(installation_id, file_id)
        resp = self._api_client.request("DELETE", path)
        return OKResponse(**resp)

    def delete_file_organization(self, organization_id: int, file_id: int):
        path = "api/v2/file/organization/{0}/{1}".format(organization_id, file_id)
        resp = self._api_client.request("DELETE", path)
        return OKResponse(**resp)

    def download_file(self, hash: str):
        path = "api/v2/file/download/{0}".format(hash)
        return self._api_client.request("GET", path, raw=True, headers={"Accept": "*/*"})

    @staticmethod
    def __multipart(file_name: str, mime: str, file):
        name = os.path.basename(file_name)
        return {name: (name, file, mime)}
