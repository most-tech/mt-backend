from dataclasses import dataclass
from dataclasses_json import dataclass_json, LetterCase


@dataclass_json
@dataclass
class SearchQuery:
    parapgraph: str
    labels: str


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class SearchResponse:
    search_results: list

    @staticmethod
    def from_result(result):
        return SearchResponse(result)
        # result can be also a list of SearchQuery elements
        # return SearchResponse([SearchQuery.from_json(element) for element in result])
        # because this part of response from elastic has the same structure as SearchQuery class
