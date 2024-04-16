import pprint
from typing import Optional


class NotificationMessage:
    def __init__(self, name: str, text: str, id: Optional[int] = None):
        self._name = name
        self._text = text
        self._id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text: str):
        self._text = text

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id: int):
        self._id = id

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "text": self.text,
        }

    def __repr__(self):
        return pprint.pformat(self.to_dict())


class NotificationOutput:
    def __init__(self, installation_id: int, name: str, notification_output_executor_id: int,
                 notification_message_id: int, config: dict[str, str], id: Optional[int] = None):
        self._installation_id = installation_id
        self._name = name
        self._notification_output_executor_id = notification_output_executor_id
        self._notification_message_id = notification_message_id
        self._config = config
        self._id = id

    @property
    def installation_id(self):
        return self._installation_id

    @installation_id.setter
    def installation_id(self, installation_id: int):
        self._installation_id = installation_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def notification_output_executor_id(self):
        return self._notification_output_executor_id

    @notification_output_executor_id.setter
    def notification_output_executor_id(self, notification_output_executor_id: int):
        self._notification_output_executor_id = notification_output_executor_id

    @property
    def notification_message_id(self):
        return self._notification_message_id

    @notification_message_id.setter
    def notification_message_id(self, notification_message_id: int):
        self._notification_message_id = notification_message_id

    @property
    def config(self):
        return self._config

    @config.setter
    def config(self, config: dict[str, str]):
        self._config = config

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id: int):
        self._id = id

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "installation_id": self.installation_id,
            "notification_message_id": self.notification_message_id,
            "notification_output_executor_id": self.notification_output_executor_id,
            "config": self.config
        }

    def __repr__(self):
        return pprint.pformat(self.to_dict())


class NotificationOutputExecutor:
    def __init__(self, type: str, name: str, organization_id: str, config: dict[str, str], id: Optional[int] = None,
                 secret: Optional[str] = None):
        self._type = type
        self._name = name
        self._organization_id = organization_id
        self._config = config
        self._id = id
        self._secret = secret

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type: str):
        self._type = type

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def organization_id(self):
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id: int):
        self._organization_id = organization_id

    @property
    def config(self):
        return self._config

    @config.setter
    def config(self, config: dict[str, str]):
        self._config = config

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id: int):
        self._id = id

    @property
    def secret(self):
        return self._secret

    @secret.setter
    def secret(self, secret: str):
        self._secret = secret

    def to_dict(self):
        return {
            "type": self.type,
            "id": self.id,
            "name": self.name,
            "organization_id": self.organization_id,
            "config": self.config,
            "secret": self.secret
        }

    def __repr__(self):
        return pprint.pformat(self.to_dict())
