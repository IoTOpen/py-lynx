import pprint


class OKResponse:
    def __init__(self, message: str):
        self._message = message

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, message: str):
        self._message = message

    def to_dict(self):
        return {
            "message": self.message
        }

    def __repr__(self):
        return pprint.pformat(self.to_dict())
