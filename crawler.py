"""
How to run?
$ python crawler.py example_batch http://www.example.com/seed/url
"""
import datetime
import sys

from crawler.application.usecase import DownloadHtmlUsecase
from crawler.batch import DownloadBatch
from crawler.domain.service import CrawlService
from crawler.infrastructure.service.web import SyncWebService
from crawler.infrastructure.repository.page import InMemoryPageRepository


args = sys.argv
BATCH_NAME = args[1]
SEED_URL = args[2]

web_service = SyncWebService()
page_repository = InMemoryPageRepository(datetime.timedelta(days=1))

DownloadBatch(
    DownloadHtmlUsecase(
        CrawlService(web_service, page_repository),
        web_service,
        page_repository,
        datetime.timedelta(days=1)
    ),
    BATCH_NAME
).download(SEED_URL)
