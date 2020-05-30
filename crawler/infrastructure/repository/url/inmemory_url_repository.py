from ....domain.model.url import URL, URLSet
from ....domain.repository import UrlRepository


class InMemoryUrlRepository(UrlRepository):

    def has_urls(self) -> bool:
        pass

    def get(self) -> URL:
        pass

    def save(self, url_set: URLSet) -> None:
        pass
