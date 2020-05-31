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
        self.url_repository.save(url)
        urls = page.get_urls()

        for other_url in urls.set:
            self.url_repository.save(other_url)
            self.recursive_crawl(other_url, i + 1, depth)

    def pagination_crawl(self, url: URL, next_page_url_regex: str, detail_url_regex) -> None:
        """
        ページネーションクロール(Pagination Crawl)

        一覧ページから詳細ページURLを保存して、次の一覧ページをクロールする

        :return:
        """
        raise NotImplementedError("未実装です")
