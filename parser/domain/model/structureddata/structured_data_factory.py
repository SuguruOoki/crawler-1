import abc

from .structured_data import StructuredData
from ..html import Html


class StructuredDataFactory(abc.ABC):

    @abc.abstractmethod
    def make_from_html(self, html: Html) -> StructuredData:
        pass

    @abc.abstractmethod
    def make_from_json(self) -> StructuredData:
        pass
