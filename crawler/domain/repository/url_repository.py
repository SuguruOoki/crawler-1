import abc

from crawler.domain.model.url import URL, URLSet


class UrlRepository(abc.ABC):

    @abc.abstractmethod
    def has_urls(self) -> bool:
        pass

    @abc.abstractmethod
    def get(self) -> URL:
        pass

    @abc.abstractmethod
    def save(self, url_set: URLSet) -> None:
        pass
