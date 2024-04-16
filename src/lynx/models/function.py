import pprint
from typing import Optional

from src.lynx.models.shared import WithMeta, Meta


class Function(WithMeta):
    def __init__(self, installation_id: int, type: str, meta: Meta,
                 protected_meta: Optional[Meta] = None,
                 id: Optional[int] = None,
                 created: Optional[int] = None,
                 updated: Optional[int] = None):
        super().__init__(meta, protected_meta)
        self._installation_id = installation_id
        self._type = type
        self._id = id
        self._created = created
        self._updated = updated

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def installation_id(self):
        return self._installation_id

    @installation_id.setter
    def installation_id(self, installation_id: int):
        self._installation_id = installation_id

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type: str):
        self._type = type

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

    def to_dict(self):
        return {
            "id": self.id,
            "installation_id": self.installation_id,
            "type": self.type,
            "meta": self.meta,
            "protected_meta": self.protected_meta,
            "created": self.created,
            "updated": self.updated,
        }

    def __repr__(self):
        return pprint.pformat(self.to_dict())
