import pprint
from typing import Optional

from src.lynx.models.shared import WithMeta, Meta, Address


class User(WithMeta):
    def __init__(self, email: str, first_name: str, last_name: str, role: int, sms_login: bool, address: Address,
                 note: str, mobile: str, organisations: list[int], meta: Meta, assigned_installations: list[int],
                 expire_at: int, protected_meta: Optional[Meta] = None, id: Optional[int] = None):
        super().__init__(meta, protected_meta)
        self._email = email
        self._first_name = first_name
        self._last_name = last_name
        self._role = role
        self._sms_login = sms_login
        self._address = address
        self._mobile = mobile
        self._organizations = organisations
        self._id = id
        self._note = note
        self._assigned_installations = assigned_installations
        self._expire_at = expire_at

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email: str):
        self._email = email

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name: str):
        self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name: str):
        self._last_name = last_name

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, role: int):
        self._role = role

    @property
    def sms_login(self):
        return self._sms_login

    @sms_login.setter
    def sms_login(self, sms_login: bool):
        self._sms_login = sms_login

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address: Address):
        self._address = address

    @property
    def mobile(self):
        return self._mobile

    @mobile.setter
    def mobile(self, mobile: str):
        self._mobile = mobile

    @property
    def organizations(self):
        return self._organizations

    @organizations.setter
    def organizations(self, organizations: list[int]):
        self._organizations = organizations

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id: int):
        self._id = id

    @property
    def note(self):
        return self._note

    @note.setter
    def note(self, note: str):
        self._note = note

    @property
    def assigned_installations(self):
        return self._assigned_installations

    @assigned_installations.setter
    def assigned_installations(self, assigned_installations: list[int]):
        self._assigned_installations = assigned_installations

    @property
    def expire_at(self):
        return self._expire_at

    @expire_at.setter
    def expire_at(self, expire_at: int):
        self._expire_at = expire_at

    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "role": self.role,
            "sms_login": self.sms_login,
            "address": self.address,
            "mobile": self.mobile,
            "organisations": self.organizations,
            "meta": self.meta,
            "protected_meta": self.protected_meta,
            "note": self.note,
            "assigned_installations": self.assigned_installations,
            "expire_at": self.expire_at,
        }

    def __repr__(self):
        return pprint.pformat(self.to_dict())
