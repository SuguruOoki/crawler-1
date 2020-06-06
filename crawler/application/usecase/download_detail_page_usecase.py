from typing import Set
from tqdm import tqdm

from crawler.domain.model.page import URL
from crawler.domain.repository import PageRepository
from crawler.domain.service import WebService


class DownloadPagesUsecase:

    def __init__(self, web_service: WebService, page_repository: PageRepository):
        self.web_service = web_service
        self.page_repository = page_repository

    def download(self, urls: Set[str]) -> None:
        """
        単一のURLページをダウンロードする.

        :param url:
        :return:
        """
        for url in tqdm(urls):
            page = self.web_service.fetch(URL(url))
            self.page_repository.save(page)
