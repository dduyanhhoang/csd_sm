import datetime
import re


class Student:
    def __init__(self, sid, name, number, yob):
        self.sid = sid
        self.name = name
        self.number = number
        self.yob = yob

    @property
    def sid(self):
        return self._sid

    @sid.setter
    def sid(self, value):
        pattern = r'^(IB|SE)(0[1-9]|1[0-9]|20)\d{4}$'
        if not re.match(pattern, value):
            raise ValueError("invalid sid")
        self._sid = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("name must be a non-empty string")
        self._name = value

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("contact number must be a non-empty string")
        self._number = value

    @property
    def yob(self):
        return self._yob

    @yob.setter
    def yob(self, value):
        if not isinstance(value, int) or value < 1900 or value > datetime.datetime.now().year:
            raise ValueError("year of birth must be a valid year")
        self._yob = value
