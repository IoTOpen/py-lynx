import pprint
import urllib.parse
from typing import Dict, Optional


class MetaObject:
    def __init__(self, value: str, protected: Optional[bool] = False):
        self._value = value
        self._protected = protected

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def protected(self):
        return self._protected

    @protected.setter
    def protected(self, value):
        self._protected = value

    def to_dict(self):
        return {
            "value": self.value,
            "protected": self.protected,
        }

    def __repr__(self):
        return pprint.pformat(self.to_dict())


class Meta(Dict[str, str]):
    def as_int(self, key: str):
        try:
            return int(self[key])
        except ValueError:
            return 0

    def as_float(self, key: str):
        try:
            return float(self[key])
        except ValueError:
            return 0.0

    def as_bool(self, key: str):
        return self[key].lower() in ["true", "1", "t", "y", "yes"]


class Filter(Dict[str, str]):
    pass


class WithMeta:
    def __init__(self, meta: Meta, protected_meta: Optional[Meta] = None):
        self._meta = meta
        self._protected_meta = protected_meta

    @property
    def meta(self):
        return self._meta

    @meta.setter
    def meta(self, meta: Meta):
        self._meta = meta

    @property
    def protected_meta(self):
        return self._protected_meta

    @protected_meta.setter
    def protected_meta(self, protected_meta: Meta):
        self._protected_meta = protected_meta

    def to_dict(self):
        return {
            "meta": self.meta,
            "protected_meta": self.protected_meta,
        }

    def __repr__(self):
        return pprint.pformat(self.to_dict())


class Address:
    def __init__(self, address: str, city: str, country: str, zip: str):
        self._address = address
        self._city = city
        self._country = country
        self._zip = zip

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address: str):
        self._address = address

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city: str):
        self._city = city

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, country: str):
        self._country = country

    @property
    def zip(self):
        return self._zip

    @zip.setter
    def zip(self, zip: str):
        self._zip = zip

    def to_dict(self):
        return {
            "address": self.address,
            "city": self.city,
            "country": self.country,
            "zip": self.zip
        }

    def __repr__(self):
        return pprint.pformat(self.to_dict())