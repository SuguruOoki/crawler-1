import datetime
from ....domain.model.page import Page
from ....domain.repository import PageRepository


class InMemoryPageRepository(PageRepository):

    def save(self, page: Page) -> None:
        pass

    def is_exist(self, page: Page) -> bool:
        pass

    def last_crawled_at(self, page: Page) -> datetime.datetime:
        pass
