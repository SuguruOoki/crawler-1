import datetime
from dataclasses import dataclass
from typing import Set

from .html import Html
from .http_status import HttpStatus
from .url import URL


@dataclass(unsafe_hash=True)
class Page:
    url: URL
    html: Html
    http_status: HttpStatus
    crawled_at: datetime.datetime

    def get_urls(self) -> Set[URL]:
        return set(URL.of(link, self.url) for link in self.html.urls())

    def should_be_saved(self, delta: datetime.timedelta) -> bool:
        return (
            self.is_200_status() and
            self.is_target() and
            self.has_times_passed_since_crawling(delta)
        )

    def should_be_downloaded(self, delta: datetime.timedelta) -> bool:
        return not (
            self.html is not None and
            self.is_200_status() and
            not self.has_times_passed_since_crawling(delta)
        )

    def is_target(self) -> bool:
        """
        Pageがクローリング対象かどうかを判定する
        
        :return: bool
        """
        return True
        # raise NotImplementedError("要件に応じて実装してください")

    def is_200_status(self) -> bool:
        return self.http_status is HttpStatus.OK

    def has_times_passed_since_crawling(self, delta: datetime.timedelta) -> bool:
        return (datetime.datetime.now() - self.crawled_at) >= delta
