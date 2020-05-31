from datetime import datetime
from datetime import timedelta

from crawler.domain.model.page import Page
from crawler.domain.model.url import URL
from crawler.domain.repository import PageRepository
from crawler.domain.repository import UrlRepository
from crawler.domain.service import CrawlService
from crawler.domain.service import WebService


class DownloadHtmlUsecase:

    def __init__(self, crawl_service: CrawlService, web_service: WebService,
                 url_repository: UrlRepository, page_repository: PageRepository,
                 delta: timedelta):
        self.crawl_service = crawl_service
        self.web_service = web_service
        self.url_repository = url_repository
        self.page_repository = page_repository
        self.delta = delta

    def download(self, seed_url: str):
        self.crawl_service.recursive_crawl(URL(seed_url))

        while self.url_repository.has_urls():
            url = self.url_repository.get()
            page = self.web_service.fetch(url)

            if self._should_save(page):
                print("保存中 {} ...".format(page.url))
                self.page_repository.save(page)
                print("保存完了")

            self.url_repository.crawled(url)
            self.crawl_service.recursive_crawl(url)

    def _should_save(self, page: Page) -> bool:
        return (
                page.is_200_status() and
                page.is_target() and
                (
                    self._page_has_not_be_crawled(page) or
                    self._has_times_passed_since_crawling(page)
                )
        )

    def _page_has_not_be_crawled(self, page: Page) -> bool:
        return not self.page_repository.is_exist(page)

    def _has_times_passed_since_crawling(self, page: Page) -> bool:
        return (datetime.now() - self.page_repository.last_crawled_at(page)) >= self.delta
