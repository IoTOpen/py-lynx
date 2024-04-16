from __future__ import annotations
import pprint
from typing import Optional, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from src.lynx import Publisher


class EdgeApp:
    def __init__(self, name: str, category: str, tags: list[str], short_description: str, description: str,
                 source_url: str, public: Optional[bool] = None, id: Optional[int] = None,
                 publisher: Optional[Publisher] = None, official: Optional[bool] = None, created: Optional[int] = None,
                 updated: Optional[int] = None):
        self._name = name
        self._category = category
        self._tags = tags
        self._short_description = short_description
        self._description = description
        self._source_url = source_url
        self._public = public
        self._id = id
        self._publisher = publisher
        self._official = official
        self._created = created
        self._updated = updated

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category: str):
        self._category = category

    @property
    def tags(self):
        return self._tags

    @tags.setter
    def tags(self, tags: list[str]):
        self._tags = tags

    @property
    def short_description(self):
        return self._short_description

    @short_description.setter
    def short_description(self, short_description: str):
        self._short_description = short_description

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description: str):
        self._description = description

    @property
    def source_url(self):
        return self._source_url

    @source_url.setter
    def source_url(self, source_url: str):
        self._source_url = source_url

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id: int):
        self._id = id

    @property
    def publisher(self):
        return self._publisher

    @publisher.setter
    def publisher(self, publisher: Publisher):
        self._publisher = publisher

    @property
    def official(self):
        return self._official

    @property
    def public(self):
        return self._public

    @public.setter
    def public(self, public: bool):
        self._public = public

    @property
    def created(self):
        return self._created

    @property
    def updated(self):
        return self._updated

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category,
            "tags": self.tags,
            "short_description": self.short_description,
            "description": self.description,
            "source_url": self.source_url,
            "publisher": self.publisher,
            "official": self.official,
            "public": self.public,
            "created": self.created,
            "updated": self.updated
        }

    def __repr__(self):
        return pprint.pformat(self.to_dict())


class EdgeAppVersion:
    def __init__(self, name: str, hash: str, timestamp: int):
        self._name = name
        self._hash = hash
        self._timestamp = timestamp

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def hash(self):
        return self._hash

    @property
    def timestamp(self):
        return self._timestamp

    def to_dict(self):
        return {
            "name": self.name,
            "hash": self.hash,
            "timestamp": self.timestamp
        }

    def __repr__(self):
        return pprint.pformat(self.to_dict())


class EdgeAppConfig:
    def __init__(self, app_id: int, installation_id: int, version: str, config: dict[str, Any], name: str,
                 id: Optional[int] = None, created: Optional[int] = None, updated: Optional[int] = None):
        self._app_id = app_id
        self._installation_id = installation_id
        self._version = version
        self._config = config
        self._name = name
        self._id = id
        self._created = created
        self._updated = updated

    @property
    def app_id(self):
        return self._app_id

    @app_id.setter
    def app_id(self, app_id: int):
        self._app_id = app_id

    @property
    def installation_id(self):
        return self._installation_id

    @installation_id.setter
    def installation_id(self, installation_id: int):
        self._installation_id = installation_id

    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, version: str):
        self._version = version

    @property
    def config(self):
        return self._config

    @config.setter
    def config(self, config: dict[str, Any]):
        self._config = config

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def id(self):
        return self._id

    @property
    def created(self):
        return self._created

    @property
    def updated(self):
        return self._updated

    def to_dict(self):
        return {
            "id": self.id,
            "app_id": self.app_id,
            "installation_id": self.installation_id,
            "version": self.version,
            "config": self.config,
            "name": self.name,
            "created": self.created,
            "updated": self.updated,
        }

    def __repr__(self):
        return pprint.pformat(self.to_dict())
