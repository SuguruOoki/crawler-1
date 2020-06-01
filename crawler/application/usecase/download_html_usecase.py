from datetime import timedelta

from crawler.domain.model.page import URL
from crawler.domain.repository import PageRepository
from crawler.domain.service import CrawlService
from crawler.domain.service import WebService


class DownloadHtmlUsecase:

    def __init__(self, crawl_service: CrawlService, web_service: WebService,
                 page_repository: PageRepository, delta: timedelta):
        self.crawl_service = crawl_service
        self.web_service = web_service
        self.page_repository = page_repository
        self.delta = delta

    def download(self, seed_url: str):
        self.crawl_service.recursive_crawl(URL(seed_url))

        while self.page_repository.has_url_should_be_downloaded():
            url = self.page_repository.get_url_should_be_downloaded()
            print("fetch {} ...".format(url))
            page = self.web_service.fetch(url)
            print("success fetch {}".format(page))

            if page.should_be_saved(self.delta):
                print("ページを保存中 {} ...".format(page.url))
                self.page_repository.save(page)
                print("保存完了")

            self.crawl_service.recursive_crawl(url)
