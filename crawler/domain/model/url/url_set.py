from dataclasses import dataclass
from typing import List

from .url import URL


@dataclass(frozen=True)
class URLSet:
    set: List[URL]

    def filter_by_domain(self, domain: str):
        return URLSet([url for url in self.set if url.domain_is(domain)])

    def filter_by_regex(self, regex: str):
        return URLSet([url for url in self.set if url.match(regex)])
