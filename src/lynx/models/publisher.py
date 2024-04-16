from __future__ import annotations
import pprint
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from src.lynx import EdgeApp


class Publisher:
    def __init__(self, name: str, id: int, apps: Optional[list[EdgeApp]] = None):
        self._name = name
        self._id = id
        self._apps = apps

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id: int):
        self._id = id

    @property
    def apps(self):
        return self._apps

    @apps.setter
    def apps(self, apps: list[EdgeApp]):
        self._apps = apps

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "apps": self.apps
        }

    def __repr__(self):
        return pprint.pformat(self.to_dict())
