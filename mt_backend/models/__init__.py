from dataclasses_json import dataclass_json
from dataclasses import dataclass
from flask import request

@dataclass_json
class Asnwer:
    pass

@dataclass_json
@dataclass
class Question:
    header : str
    body : str

    @staticmethod
    def from_get(value):
        header = ""
        body = value
        return Question(header=header, body=body)
