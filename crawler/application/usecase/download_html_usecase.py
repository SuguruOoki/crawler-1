from datetime import datetime
from datetime import timedelta

from crawler.domain.model.page import Page
from crawler.domain.model.url import URL
from crawler.domain.repository import PageRepository
from crawler.domain.repository import UrlRepository
from crawler.domain.service import WebService


class DownloadHtmlUsecase:

    def __init__(self, web_service: WebService, url_repository: UrlRepository, page_repository: PageRepository):
        self.web_service = web_service
        self.url_repository = url_repository
        self.page_repository = page_repository

    def download(self, seed_url: str):
        self._crawling(URL(seed_url))

        while self.url_repository.has_urls():
            url = self.url_repository.get()
            page = self.web_service.fetch(url)

            if self._should_page_save(page):
                self.page_repository.save(page)

            self._crawling(url)

    def _crawling(self, url: URL, i=0, depth=0) -> None:
        """
        起点となるURLから、n回まで再帰的にURLをクローリングして、保存する。

        :param url:
        :param i:
        :param n:
        :return:
        """
        if i > depth:
            return

        page = self.web_service.fetch(url)
        urls = page.get_urls()
        self.url_repository.save(urls)

        for url in urls.set:
            self._crawling(url, i + 1, depth)

    def _should_page_save(self, page: Page) -> bool:
        return (
            page.is_200_status() and
            page.is_target() and
            (self._is_not_crawled(page) or self._has_times_passed_since_crawling(page))
        )

    def _is_not_crawled(self, page: Page) -> bool:
        return not self.page_repository.is_exist(page)

    def _has_times_passed_since_crawling(self, page: Page, delta: timedelta) -> bool:
        return (datetime.now() - self.page_repository.last_crawled_at(page)) >= delta
