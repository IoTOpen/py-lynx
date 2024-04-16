import pprint
from typing import Optional

from src.lynx.models.shared import WithMeta, Meta, Address


class OrganizationChild:
    def __init__(self, id: int, name: str):
        self._id = id
        self._name = name

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }

    def __repr__(self):
        return pprint.pformat(self.to_dict())


class Organization(WithMeta):
    def __init__(self, name: str, parent: int, address: Optional[Address] = None, email: Optional[str] = None,
                 phone: Optional[str] = None, force_sms_login: Optional[bool] = None, notes: Optional[str] = None,
                 password_valid_days: Optional[int] = None, meta: Optional[Meta] = None,
                 protected_meta: Optional[Meta] = None, id: Optional[int] = None,
                 children: Optional[list[OrganizationChild]] = None):
        super().__init__(meta, protected_meta)
        self._name = name
        self._address = address
        self._email = email
        self._phone = phone
        self._force_sms_login = force_sms_login
        self._parent = parent
        self._children = children
        self._notes = notes
        self._password_valid_days = password_valid_days
        self._id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address: Address):
        self._address = address

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email: str):
        self._email = email

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone: str):
        self._phone = phone

    @property
    def force_sms_login(self):
        return self._force_sms_login

    @force_sms_login.setter
    def force_sms_login(self, force_sms_login: bool):
        self._force_sms_login = force_sms_login

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, parent: int):
        self._parent = parent

    @property
    def children(self):
        return self._children

    @property
    def notes(self):
        return self._notes

    @notes.setter
    def notes(self, notes: str):
        self._notes = notes

    @property
    def password_valid_days(self):
        return self._password_valid_days

    @password_valid_days.setter
    def password_valid_days(self, password_valid_days: int):
        self._password_valid_days = password_valid_days

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
            "address": self.address,
            "email": self.email,
            "phone": self.phone,
            "force_sms_login": self.force_sms_login,
            "parent": self.parent,
            "children": self.children,
            "notes": self.notes,
            "password_valid_days": self.password_valid_days,
            "meta": self.meta,
            "protected_meta": self.protected_meta,
        }

    def __repr__(self):
        return pprint.pformat(self.to_dict())
