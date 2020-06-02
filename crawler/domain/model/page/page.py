from datetime import datetime
from dataclasses import dataclass

from .html import Html
from .http_status import HttpStatus
from ..url import URL, URLSet


@dataclass(unsafe_hash=True)
class Page:
    url: URL
    html: Html
    http_status: HttpStatus
    crawled_at: datetime

    def get_urls(self) -> URLSet:
        return URLSet(set(URL.of(link, self.url) for link in self.html.urls()))

    def is_target(self) -> bool:
        """
        Pageがクローリング対象かどうかを判定する
        
        :return: bool
        """
        raise NotImplementedError("要件に応じて実装してください")

    def is_200_status(self) -> bool:
        return self.http_status is HttpStatus.OK
