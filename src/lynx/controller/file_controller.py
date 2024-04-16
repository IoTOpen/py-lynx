from src.lynx import File, OKResponse
from src.lynx.api_client import APIClient
from src.lynx.controller import Controller


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
        raise Exception("Not implemented")

    def create_file_organization(self, organization_id: int, file_name: str, mime: str, file):
        raise Exception("Not implemented")

    def update_file_installation(self, installation_id: int, file_name: str, mime: str, file):
        raise Exception("Not implemented")

    def update_file_organization(self, organization_id: int, file_name: str, mime: str, file):
        raise Exception("Not implemented")

    def delete_file_installation(self, installation_id: int, file_id: int):
        path = "api/v2/file/installation/{0}/{1}".format(installation_id, file_id)
        resp = self._api_client.request("DELETE", path)
        return OKResponse(**resp)

    def delete_file_organization(self, organization_id: int, file_id: int):
        path = "api/v2/file/organization/{0}/{1}".format(organization_id, file_id)
        resp = self._api_client.request("DELETE", path)
        return OKResponse(**resp)

    def download_file(self, hash: str):
        raise Exception("Not implemented")
