import pprint
from typing import Optional


class File:
    def __init__(self, hash: str, name: str, mime: str, id: Optional[int] = None, installation_id: Optional[int] = None,
                 organization_id: Optional[int] = None, created: Optional[int] = None, updated: Optional[int] = None):
        self._hash = hash
        self._name = name
        self._mime = mime
        self._id = id
        self._installation_id = installation_id
        self._organization_id = organization_id
        self._created = created
        self._updated = updated

    @property
    def hash(self):
        return self._hash

    @property
    def name(self):
        return self._name

    @property
    def mime(self):
        return self._mime

    @property
    def id(self):
        return self._id

    @property
    def installation_id(self):
        return self._installation_id

    @property
    def organization_id(self):
        return self._organization_id

    @property
    def created(self):
        return self._created

    @property
    def updated(self):
        return self._updated

    def to_dict(self):
        return {
            "hash": self.hash,
            "name": self.name,
            "mime": self.mime,
            "id": self.id,
            "installation_id": self.installation_id,
            "organization_id": self.organization_id,
            "created": self.created,
            "updated": self.updated
        }

    def __repr__(self):
        return pprint.pformat(self.to_dict())
