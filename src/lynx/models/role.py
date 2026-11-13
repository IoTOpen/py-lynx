import pprint
from typing import Optional


class Role:
    def __init__(self, name: str, permissions: dict[str, bool], priority: int, id: Optional[int] = None):
        self._name = name
        self._permissions = permissions
        self._priority = priority
        self._id = id

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id: int):
        self._id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def permissions(self):
        return self._permissions

    @permissions.setter
    def permissions(self, permissions: dict[str, bool]):
        self._permissions = permissions

    @property
    def priority(self):
        return self._priority

    @priority.setter
    def priority(self, priority: int):
        self._priority = priority

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "permissions": self.permissions,
            "priority": self.priority,
        }

    def __repr__(self):
        return pprint.pformat(self.to_dict())
