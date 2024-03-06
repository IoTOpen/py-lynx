import pprint


class LogEntry:
    def __init__(self, client_id: int, installation_id: int, msg: str, timestamp: float, topic: str, value: float):
        self._client_id = client_id
        self._installation_id = installation_id
        self._msg = msg
        self._timestamp = timestamp
        self._topic = topic
        self._value = value

    @property
    def client_id(self):
        return self._client_id

    @property
    def installation_id(self):
        return self._installation_id

    @property
    def msg(self):
        return self._msg

    @property
    def timestamp(self):
        return self._timestamp

    @property
    def topic(self):
        return self._topic

    @property
    def value(self):
        return self._value

    def to_dict(self):
        return {
            "client_id": self.client_id,
            "installation_id": self.installation_id,
            "msg": self.msg,
            "timestamp": self.timestamp,
            "topic": self.topic,
            "value": self.value,
        }

    def __repr__(self):
        return pprint.pformat(self.to_dict())


class LogPage:
    def __init__(self, total: int, last: float, count: int, data: list[LogEntry]):
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
            "last": self.last,
            "count": self.count,
            "data": self.data
        }

    def __repr__(self):
        return pprint.pformat(self.to_dict())
