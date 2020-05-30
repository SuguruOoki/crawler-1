import abc

from ..model.page import Page
from ..model.url import URL


class WebService(abc.ABC):

    @abc.abstractmethod
    def fetch(self, url: URL) -> Page:
        pass
