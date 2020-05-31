from bs4 import BeautifulSoup
from dataclasses import dataclass
from typing import List

from .character_code import CharacterCode


@dataclass(frozen=True)
class Html:
    text: str
    character_code: CharacterCode

    def urls(self) -> List[str]:
        return [link.get("href") for link in BeautifulSoup(self.text, 'html.parser').find_all("a")]
