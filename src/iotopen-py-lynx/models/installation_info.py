import pprint
from typing import Optional

from src.lynx.models.shared import WithMeta, Meta


class InstallationInfo:
    def __init__(self, name: str, organization_id: int, id: int, client_id: int, assigned: bool,
                 capabilities: list[str]):
        self._name = name
        self._organization_id = organization_id
        self._id = id
        self._client_id = client_id
        self._assigned = assigned
        self._capabilities = capabilities

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id: int):
        self._id = id

    @property
    def client_id(self):
        return self._client_id

    @client_id.setter
    def client_id(self, client_id: int):
        self._client_id = client_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def capabilities(self):
        return self._capabilities

    @capabilities.setter
    def capabilities(self, capabilities: list[str]):
        self._capabilities = capabilities

    @property
    def organization_id(self):
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id: int):
        self._organization_id = organization_id

    @property
    def assigned(self):
        return self._assigned

    @assigned.setter
    def assigned(self, assigned: bool):
        self._assigned = assigned

    def to_dict(self):
        return {
            "id": self.id,
            "client_id": self.client_id,
            "name": self.name,
            "capabilities": self.capabilities,
            "organization_id": self.organization_id,
            "assigned": self.assigned,
        }

    def __repr__(self):
        return pprint.pformat(self.to_dict())
