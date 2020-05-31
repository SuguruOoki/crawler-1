import datetime
import time

from ....domain.model.url import URL, URLSet
from ....domain.repository import UrlRepository


class InMemoryUrlRepository(UrlRepository):
    urls = dict()

    def has_urls(self) -> bool:
        return len(self.urls) > 0

    def get(self, timedelta: datetime.timedelta) -> URL:
        for url, hist in self.urls.items():
            if hist["status"] == "not crawl":
                return url
            if (datetime.datetime.now() - hist["crawled_at"]) >= timedelta:
                return url

    def save(self, url_set: URLSet) -> None:
        for url in url_set.set:
            if url in self.urls.keys():
                continue
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
