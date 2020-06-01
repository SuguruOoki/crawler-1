from tqdm import tqdm
from .web_service import WebService
from ..model.page import URL
from ..repository import PageRepository


class CrawlService:

    def __init__(self, web_service: WebService, page_repository: PageRepository):
        self.web_service = web_service
        self.page_repository = page_repository

    def recursive_crawl(self, url: URL, i=0, depth=0) -> None:
        """
        再帰的クロール(Recursive Crawl)

        起点となるURLから、n回まで再帰的にURLをクローリングして、保存する。

        :param url:
        :param i:
        :param depth:
        :return:
        """
        page = self.web_service.fetch(url)
        self.page_repository.save(page)

        if i > depth:
            return

        print("{}階層をクローリング中 ...".format(i + 1))
        for other_url in tqdm(page.get_urls()):
            self.recursive_crawl(other_url, i + 1, depth)

    def pagination_crawl(self, url: URL, list_page_url_regex: str, detail_page_url_regex) -> None:
        """
        ページネーションクロール(Pagination Crawl)

        一覧ページURL(List Page URL)から詳細ページURL(Detail Page URL)を保存して、次の一覧ページをクロールする

        :return:
        """
        raise NotImplementedError("未実装です")
