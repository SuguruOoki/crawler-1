import abc
import datetime

from ..model.page import Page


class PageRepository(abc.ABC):

    @abc.abstractmethod
    def save(self, page: Page) -> None:
        raise NotImplementedError("infrastructureパッケージで実装してください")

    @abc.abstractmethod
    def is_exist(self, page: Page) -> bool:
        raise NotImplementedError("infrastructureパッケージで実装してください")

    @abc.abstractmethod
    def last_crawled_at(self, page: Page) -> datetime.datetime:
        raise NotImplementedError("infrastructureパッケージで実装してください")
