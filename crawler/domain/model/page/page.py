from datetime import datetime
from dataclasses import dataclass

from .html import Html
from .http_status import HttpStatus
from ..url import URL, URLSet


@dataclass
class Page:
    url: URL
    html: Html
    http_status: HttpStatus
    crawled_at: datetime

    def get_urls(self) -> URLSet:
        return self.html.urls()

    def is_target(self) -> bool:
        """
        Pageがクローリング対象かどうかを判定する
        
        :return: bool
        """
        raise NotImplementedError("要件に応じて実装してください")