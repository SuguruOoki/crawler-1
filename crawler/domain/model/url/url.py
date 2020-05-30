from datetime import datetime
from dataclasses import dataclass


@dataclass
class URL:
    url: str
    crawled_at: datetime

    def domain_is(self, domain: str) -> bool:
        return True

    def match(self, regex: str) -> bool:
        return True
