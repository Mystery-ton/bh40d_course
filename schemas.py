from pydantic import BaseModel
from pydantic_core import ValidationError
from typing import *
from csv import DictReader, reader, writer, DictWriter


class UserDetail(BaseModel):
    id: int
    surname: str
    email: str


data = {"id": 34, "surname": "Alex", "email": "alex@"}
try:
    user_detail = UserDetail(**data)
except ValidationError as e:
    print(e.errors())


class SimpleSchema(BaseModel):
    name: str
    surname: str
    email: str = None

    @classmethod
    def from_csv(cls, file):
        data = []
        r = DictReader(file)
        for line in r:
            obj = cls(name=line["name"], surname=line["surname"], email=line["email"])
            data.append(obj)

        return data

    def to_csv(self, file):
        w = writer(file)
        w.writerow([self.name, self.surname, self.email])
