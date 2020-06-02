from pid.decorator import pidfile

from ...domain.model.structureddata import StructuredDataFactory
from ...domain.repository import HtmlRepository, StructuredDataRepository


class ParseHtmlUsecase:

    def __init__(self, html_repository: HtmlRepository,
                 structured_data_factory: StructuredDataFactory,
                 structured_data_repository: StructuredDataRepository):
        self.html_repository = html_repository
        self.structured_data_factory = structured_data_factory
        self.structured_data_repository = structured_data_repository

    @pidfile()
    def parse(self) -> None:
        while self.html_repository.has_new_html():
            self._parse()

    def _parse(self) -> None:
        html = self.html_repository.pop()
        structured_data = self.structured_data_factory.make_from_html(html)
        self.structured_data_repository.save(structured_data)