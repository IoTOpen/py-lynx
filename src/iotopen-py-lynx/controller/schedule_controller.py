from typing import Optional

from src.lynx import Device, OKResponse, Schedule
from src.lynx.api_client import APIClient
from src.lynx.controller import Controller


class ScheduleController(Controller):
    def __init__(self, api_client: APIClient):
        super().__init__(api_client)

    def get_schedules(self, installation_id: int, executor: Optional[str] = None):
        qs = ""
        if executor:
            qs = self.format_query_string(dict({"executor": executor}))

        path = "api/v2/schedule/{0}{1}".format(installation_id, qs)
        resp = self._api_client.request("GET", path)
        res = []
        for x in resp:
            res.append(Schedule(**x))
        return res

    def get_schedule(self, installation_id: int, id: int):
        path = "api/v2/schedule/{0}/{1}".format(installation_id, id)
        resp = self._api_client.request("GET", path)
        return Schedule(**resp)

    def create_schedule(self, schedule: Schedule):
        path = "api/v2/schedule/{0}".format(schedule.installation_id)
        resp = self._api_client.request("POST", path, json=schedule.to_dict())
        return Schedule(**resp)

    def update_schedule(self, schedule: Schedule):
        path = "api/v2/schedule/{0}/{1}".format(schedule.installation_id, schedule.id)
        resp = self._api_client.request("PUT", path, json=schedule.to_dict())
        return Schedule(**resp)

    def delete_schedule(self, schedule: Schedule):
        path = "api/v2/schedule/{0}/{1}".format(schedule.installation_id, schedule.id)
        resp = self._api_client.request("DELETE", path)
        return OKResponse(**resp)
