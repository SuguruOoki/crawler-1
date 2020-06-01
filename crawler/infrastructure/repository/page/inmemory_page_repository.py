import datetime
from ....domain.model.page import Page, URL
from ....domain.repository import PageRepository


class InMemoryPageRepository(PageRepository):
    pages = set()

    def __init__(self, delta: datetime.timedelta):
        self.delta = delta

    def has_url_should_be_downloaded(self) -> bool:
        for page in self.pages:
            if page.should_be_downloaded(self.delta):
                return True

    def get_url_should_be_downloaded(self) -> URL:
        for page in self.pages:
            if page.should_be_downloaded(self.delta):
                return page.url

    def save(self, page: Page) -> None:
        self.pages.add(page)

    def is_exist(self, page: Page) -> bool:
        return page in self.pages
