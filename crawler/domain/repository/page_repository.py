import abc

from ..model.page import Page, URL


class PageRepository(abc.ABC):

    @abc.abstractmethod
    def has_url_should_be_downloaded(self) -> bool:
        raise NotImplementedError("infrastructureパッケージで実装してください")

    @abc.abstractmethod
    def get_url_should_be_downloaded(self) -> URL:
        raise NotImplementedError("infrastructureパッケージで実装してください")

    @abc.abstractmethod
    def save(self, page: Page) -> None:
        raise NotImplementedError("infrastructureパッケージで実装してください")

    @abc.abstractmethod
    def is_exist(self, page: Page) -> bool:
        raise NotImplementedError("infrastructureパッケージで実装してください")

