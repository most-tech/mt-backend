from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class SearchQuery:
    keystroke: str
    labels: str


@dataclass_json
@dataclass
class SearchResponse:
    responses: list

    @staticmethod
    def from_result(result):
        return SearchResponse(result)
        # result can be also a list of SearchQuery elements
        # return SearchResponse([SearchQuery.from_json(element) for element in result])
        # because this part of response from elastic has the same structure as SearchQuery class
