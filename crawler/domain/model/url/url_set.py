from dataclasses import dataclass
from typing import Set

from .url import URL


@dataclass(frozen=True)
class URLSet:
    set: Set[URL]

    def filter_by_regex(self, regex: str):
        return URLSet(set(url for url in self.set if url.match(regex)))
