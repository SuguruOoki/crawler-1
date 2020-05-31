import datetime

from ....domain.model.url import URL, URLSet
from ....domain.repository import UrlRepository


class InMemoryUrlRepository(UrlRepository):
    urls = dict()

    def __init__(self, update_delta: datetime.timedelta):
        self.update_delta = update_delta

    def has_urls(self) -> bool:
        for hist in self.urls.values():
            if (hist['status'] == "not crawl") or self._should_url_be_updated(hist['crawled_at']):
                return True
        return False

    def get(self) -> URL:
        for url, hist in self.urls.items():
            if (hist["status"] == "not crawl") or self._should_url_be_updated(hist['crawled_at']):
                return url

    def save(self, url: URL) -> None:
        if url in self.urls.keys():
            return

        self.urls.update({
            url: {
                "status": "not crawl",
                "crawled_at": datetime.datetime.now()
            }
        })

    def crawled(self, url: URL) -> None:
        self.urls.update({
            url: {
                "status": "crawled",
                "crawled_at": datetime.datetime.now()
            }
        })

    def _should_url_be_updated(self, crawled_at: datetime.datetime) -> bool:
        return (datetime.datetime.now() - crawled_at) >= self.update_delta
