import abc

from ..model.page import Page, URL


class WebService(abc.ABC):

    @abc.abstractmethod
    def fetch(self, url: URL) -> Page:
        pass
