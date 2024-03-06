import pprint

from src.lynx.models import TraceAction, TraceObjectType


class TraceEntry:
    def __init__(self, id: str, path: str, method: str, timestamp: float, user_id: int, action: TraceAction,
                 object_type: TraceObjectType, object_id: int, description: str):
        self._id = id
        self._path = path
        self._method = method
        self._timestamp = timestamp
        self._user_id = user_id
        self._action = action
        self._object_type = object_type
        self._object_id = object_id
        self._description = description

    @property
    def id(self):
        return self._id

    @property
    def path(self):
        return self._path

    @property
    def method(self):
        return self._method

    @property
    def timestamp(self):
        return self._timestamp

    @property
    def user_id(self):
        return self._user_id

    @property
    def action(self):
        return self._action

    @property
    def object_type(self):
        return self._object_type

    @property
    def object_id(self):
        return self._object_id

    @property
    def description(self):
        return self._description

    def to_dict(self):
        return {
            "id": self.id,
            "path": self.path,
            "method": self.method,
            "timestamp": self.timestamp,
            "user_id": self.user_id,
            "action": self.action,
            "object_type": self.object_type,
            "object_id": self.object_id,
            "description": self.description
        }

    def __repr__(self):
        return pprint.pformat(self.to_dict())


class TracePage:
    def __init__(self, total: int, last: float, count: int, data: list[TraceEntry]):
        self._total = total
        self._last = last
        self._count = count
        self._data = data

    @property
    def total(self):
        return self._total

    @property
    def last(self):
        return self._last

    @property
    def count(self):
        return self._count

    @property
    def data(self):
        return self._data

    def to_dict(self):
        return {
            "total": self.total,
            "last_time": self.last,
            "count": self.count,
            "data": self.data
        }

    def __repr__(self):
        return pprint.pformat(self.to_dict())
