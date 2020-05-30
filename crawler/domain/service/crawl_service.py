from .web_service import WebService
from ..model.url import URL
from ..repository import UrlRepository


class CrawlService:

    def __init__(self, web_service: WebService, url_repository: UrlRepository):
        self.web_service = web_service
        self.url_repository = url_repository

    def recursive_crawl(self, url: URL, i=0, depth=0) -> None:
        """
        再帰的クロール(Recursive Crawl)

        起点となるURLから、n回まで再帰的にURLをクローリングして、保存する。

        :param url:
        :param i:
        :param depth:
        :return:
        """
        if i > depth:
            return

        page = self.web_service.fetch(url)
        urls = page.get_urls()
        self.url_repository.save(urls)

        for url in urls.set:
            self.recursive_crawl(url, i + 1, depth)
