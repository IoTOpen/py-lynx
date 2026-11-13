from .. import OKResponse
from ..api_client import APIClient
from ..controller import Controller


class MQTTController(Controller):
    def __init__(self, api_client: APIClient):
        super().__init__(api_client)

    def publish(self, installation_id: int, topic: str, payload: any):
        path = "api/v2/mqtt/publish/{0}".format(installation_id)
        resp = self._api_client.request("POST", path, json={"topic": topic, "payload": payload})
        return OKResponse(**resp)
