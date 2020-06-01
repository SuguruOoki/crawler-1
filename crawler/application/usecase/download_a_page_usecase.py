from crawler.domain.model.page import URL
from crawler.domain.repository import PageRepository
from crawler.domain.service import WebService


class DownloadAPageUsecase:

    def __init__(self, web_service: WebService, page_repository: PageRepository):
        self.web_service = web_service
        self.page_repository = page_repository

    def download(self, url: str) -> None:
        """
        単一のURLページをダウンロードする.

        :param url:
        :return:
        """
        page = self.web_service.fetch(URL(url))
        self.page_repository.save(page)
