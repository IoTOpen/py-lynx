from typing import Optional

from src.lynx import NotificationMessage, NotificationOutput, OKResponse, NotificationOutputExecutor
from src.lynx.api_client import APIClient
from src.lynx.controller import Controller


class NotificationController(Controller):
    def __init__(self, api_client: APIClient):
        super().__init__(api_client)

    def get_notification_messages(self, installation_id: int):
        path = "api/v2/notification/{0}/message".format(installation_id)
        resp = self._api_client.request("GET", path)
        res = []
        for x in resp:
            res.append(NotificationMessage(**x))
        return res

    def get_notification_message(self, installation_id: int, id: int):
        path = "api/v2/notification/{0}/message/{1}".format(installation_id, id)
        resp = self._api_client.request("GET", path)
        return NotificationMessage(**resp)

    def create_notification_message(self, installation_id: int, notification_message: NotificationMessage):
        path = "api/v2/notification/{0}/message".format(installation_id)
        resp = self._api_client.request("POST", path, json=notification_message.to_dict())
        return NotificationMessage(**resp)

    def update_notification_message(self, installation_id: int, notification_message: NotificationMessage):
        path = "api/v2/notification/{0}/message/{1}".format(installation_id, notification_message.id)
        resp = self._api_client.request("PUT", path, json=notification_message.to_dict())
        return NotificationMessage(**resp)

    def delete_notification_message(self, installation_id: int, notification_message: NotificationMessage):
        path = "api/v2/notification/{0}/message/{1}".format(installation_id, notification_message.id)
        resp = self._api_client.request("DELETE", path, json=notification_message.to_dict())
        return NotificationMessage(**resp)

    def get_notification_outputs(self, installation_id: int):
        path = "api/v2/notification/{0}/output".format(installation_id)
        resp = self._api_client.request("GET", path)
        res = []
        for x in resp:
            res.append(NotificationOutput(**x))
        return res

    def get_notification_output(self, installation_id: int, id: int):
        path = "api/v2/notification/{0}/output/{1}".format(installation_id, id)
        resp = self._api_client.request("GET", path)
        return NotificationOutput(**resp)

    def create_notification_output(self, notification_output: NotificationOutput):
        path = "api/v2/notification/{0}/output".format(notification_output.installation_id)
        resp = self._api_client.request("POST", path, json=notification_output.to_dict())
        return NotificationOutput(**resp)

    def update_notification_output(self, notification_output: NotificationOutput):
        path = "api/v2/notification/{0}/output/{1}".format(notification_output.installation_id, notification_output.id)
        resp = self._api_client.request("PUT", path, json=notification_output.to_dict())
        return NotificationOutput(**resp)

    def delete_notification_output(self, notification_output: NotificationOutput):
        path = "api/v2/notification/{0}/output/{1}".format(notification_output.installation_id, notification_output.id)
        resp = self._api_client.request("DELETE", path)
        return OKResponse(**resp)

    def get_notification_output_executors(self, installation_id: int):
        path = "api/v2/notification/{0}/executor".format(installation_id)
        resp = self._api_client.request("GET", path)
        res = []
        for x in resp:
            res.append(NotificationOutputExecutor(**x))
        return res

    def get_notification_output_executor(self, installation_id: int, id: int):
        path = "api/v2/notification/{0}/executor/{1}".format(installation_id, id)
        resp = self._api_client.request("GET", path)
        return NotificationOutputExecutor(**resp)

    def send_notification(self, installation_id: int, output_id: int, data: Optional[dict[str, any]] = None):
        path = "api/v2/notification/{0}/output/{1}/send".format(installation_id, output_id)
        if not data:
            data = dict()
        resp = self._api_client.request("POST", path, json=data)
        return OKResponse(**resp)
