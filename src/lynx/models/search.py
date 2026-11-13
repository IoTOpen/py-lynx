import pprint
from typing import Optional


class SearchEntry:
    def __init__(self, type: str, id: int, name: str, description: Optional[str] = None, notes: Optional[str] = None,
                 created: Optional[int] = None, updated: Optional[int] = None, client_id: Optional[int] = None,
                 installation_id: Optional[int] = None, organization_id: Optional[int] = None,
                 meta_matches: Optional[dict[str, str]] = None, metadata: Optional[dict[str, str]] = None):
        self._type = type
        self._id = id
        self._name = name
        self._description = description
        self._notes = notes
        self._created = created
        self._updated = updated
        self._client_id = client_id
        self._installation_id = installation_id
        self._organization_id = organization_id
        self._meta_matches = meta_matches
        self._metadata = metadata

    @property
    def type(self):
        return self._type

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @property
    def notes(self):
        return self._notes

    @property
    def created(self):
        return self._created

    @property
    def updated(self):
        return self._updated

    @property
    def client_id(self):
        return self._client_id

    @property
    def installation_id(self):
        return self._installation_id

    @property
    def organization_id(self):
        return self._organization_id

    @property
    def meta_matches(self):
        return self._meta_matches

    @property
    def metadata(self):
        return self._metadata

    def to_dict(self):
        return {
            "type": self.type,
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "notes": self.notes,
            "created": self.created,
            "updated": self.updated,
            "client_id": self.client_id,
            "installation_id": self.installation_id,
            "organization_id": self.organization_id,
            "meta_matches": self.meta_matches,
            "metadata": self.metadata,
        }

    def __repr__(self):
        return pprint.pformat(self.to_dict())


class SearchResult:
    def __init__(self, total: int, limit: int, offset: int, results: list[SearchEntry]):
        self._total = total
        self._limit = limit
        self._offset = offset
        self._results = results

    @property
    def total(self):
        return self._total

    @property
    def limit(self):
        return self._limit

    @property
    def offset(self):
        return self._offset

    @property
    def results(self):
        return self._results

    def to_dict(self):
        return {
            "total": self.total,
            "limit": self.limit,
            "offset": self.offset,
            "results": self.results,
        }

    def __repr__(self):
        return pprint.pformat(self.to_dict())
