from bs4 import BeautifulSoup
from dataclasses import dataclass
from typing import Set

from .character_code import CharacterCode


@dataclass(frozen=True)
class Html:
    text: str
    character_code: CharacterCode

    def urls(self) -> Set[str]:
        if self.text is None:
            return set()

        urls = set()
        for link in BeautifulSoup(self.text, 'html.parser').find_all("a"):
            if link.get("href") is not None:
                urls.add(link.get("href"))
        return urls
