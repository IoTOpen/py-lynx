import pprint
from typing import Optional

from src.lynx.models.shared import WithMeta, Meta


class Installation(WithMeta):
    def __init__(self, name: str, organization_id: int, notes: str, users: list[int], meta: Meta,
                 id: Optional[int] = None, client_id: Optional[int] = None, protected_meta: Optional[Meta] = None,
                 created: Optional[int] = None):
        super().__init__(meta, protected_meta)
        self._name = name
        self._organization_id = organization_id
        self._notes = notes
        self._users = users
        self._id = id
        self._client_id = client_id
        self._created = created

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
    def client_id(self):
        return self._client_id

    @client_id.setter
    def client_id(self, client_id: int):
        self._client_id = client_id

    @property
    def created(self):
        return self._created

    @created.setter
    def created(self, created: int):
        self._created = created

    @property
    def organization_id(self):
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id: int):
        self._organization_id = organization_id

    @property
    def notes(self):
        return self._notes

    @notes.setter
    def notes(self, notes: str):
        self._notes = notes

    @property
    def users(self):
        return self._users

    @users.setter
    def users(self, users: list[int]):
        self._users = users

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "client_id": self.client_id,
            "created": self.created,
            "organization_id": self.organization_id,
            "notes": self.notes,
            "users": self.users,
            "meta": self.meta,
            "protected_meta": self.protected_meta,
        }

    def __repr__(self):
        return pprint.pformat(self.to_dict())
