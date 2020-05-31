"""
How to run?
$ python crawler.py example_batch http://www.example.com/seed/url
"""
import sys

from crawler.application.usecase import DownloadHtmlUsecase
from crawler.batch import DownloadBatch
from crawler.infrastructure.service.web import SyncWebService
from crawler.infrastructure.repository.url import InMemoryUrlRepository
from crawler.infrastructure.repository.page import InMemoryPageRepository


args = sys.argv
BATCH_NAME = args[1]
SEED_URL = args[2]

DownloadBatch(
    DownloadHtmlUsecase(
        SyncWebService(),
        InMemoryUrlRepository(),
        InMemoryPageRepository()
    ),
    BATCH_NAME
).download(SEED_URL)
