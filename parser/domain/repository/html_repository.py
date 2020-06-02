import abc

from ..model.html import Html


class HtmlRepository(abc.ABC):

    @abc.abstractmethod
    def pop(self) -> Html:
        pass

    @abc.abstractmethod
    def has_new_html(self) -> Html:
        pass
