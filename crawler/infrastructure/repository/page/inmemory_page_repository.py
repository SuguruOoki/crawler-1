import datetime
from ....domain.model.page import Page
from ....domain.repository import PageRepository


class InMemoryPageRepository(PageRepository):
    pages = set()

    def save(self, page: Page) -> None:
        self.pages.add(page)

    def is_exist(self, page: Page) -> bool:
        return page in self.pages

    def last_crawled_at(self, page: Page) -> datetime.datetime:
        pass
