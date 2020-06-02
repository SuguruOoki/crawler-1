from dataclasses import dataclass

from .url import URL


@dataclass(frozen=True)
class Html:
    url: URL
    text: str
