import pprint
from typing import Optional


class Schedule:
    def __init__(self, installation_id: int, executor: str, active: bool, day_of_week: str, day_of_month: str,
                 month: str, hour: str, minute: str, topic: str, value: float, created_at: Optional[int] = None,
                 updated_at: Optional[int] = None, id: Optional[int] = None):
        self._installation_id = installation_id
        self._executor = executor
        self._active = active
        self._day_of_week = day_of_week
        self._day_of_month = day_of_month
        self._month = month
        self._hour = hour
        self._minute = minute
        self._topic = topic
        self._value = value
        self._created = created_at
        self._updated = updated_at
        self._id = id

    @property
    def installation_id(self):
        return self._installation_id

    @installation_id.setter
    def installation_id(self, installation_id: int):
        self._installation_id = installation_id

    @property
    def executor(self):
        return self._executor

    @executor.setter
    def executor(self, executor: str):
        self._executor = executor

    @property
    def active(self):
        return self._active

    @active.setter
    def active(self, active: bool):
        self._active = active

    @property
    def day_of_week(self):
        return self._day_of_week

    @day_of_week.setter
    def day_of_week(self, day_of_week: str):
        self._day_of_week = day_of_week

    @property
    def day_of_month(self):
        return self._day_of_month

    @day_of_month.setter
    def day_of_month(self, day_of_month: str):
        self._day_of_month = day_of_month

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, month: str):
        self._month = month

    @property
    def hour(self):
        return self._hour

    @hour.setter
    def hour(self, hour: str):
        self._hour = hour

    @property
    def minute(self):
        return self._minute

    @minute.setter
    def minute(self, minute: str):
        self._minute = minute

    @property
    def topic(self):
        return self._topic

    @topic.setter
    def topic(self, topic: str):
        self._topic = topic

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value: float):
        self._value = value

    @property
    def created(self):
        return self._created

    @created.setter
    def created(self, created: int):
        self._created = created

    @property
    def updated(self):
        return self._updated

    @updated.setter
    def updated(self, updated: int):
        self._updated = updated

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id: int):
        self._id = id

    def to_dict(self):
        return {
            "id": self.id,
            "installation_id": self.installation_id,
            "executor": self.executor,
            "active": self.active,
            "day_of_week": self.day_of_week,
            "dat_of_month": self.day_of_month,
            "month": self.month,
            "hour": self.hour,
            "minute": self.minute,
            "topic": self.topic,
            "value": self.value,
            "created_at": self.created,
            "updated_at": self.updated,
        }

    def __repr__(self):
        return pprint.pformat(self.to_dict())
