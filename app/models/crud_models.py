from dataclasses import dataclass, field
from typing import List
from dataclasses_json import dataclass_json
from dataclasses_json import LetterCase


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class LegalDocument:
    paragraph: str
    header: str
    link: str
    labels: List[str] = field(default_factory=list)
