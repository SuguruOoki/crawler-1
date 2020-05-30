"""
How to run?
$ python crawler.py http://www.example.com/seed/url
"""
import sys

from .application.usecase import DownloadHtmlUsecase
from .batch import DownloadBatch
from .infrastructure.service.web import SyncWebService
from .infrastructure.repository.url import InMemoryUrlRepository
from .infrastructure.repository.page import InMemoryPageRepository


args = sys.argv
SEED_URL = args[0]

DownloadBatch(
    DownloadHtmlUsecase(
        SyncWebService(),
        InMemoryUrlRepository(),
        InMemoryPageRepository()
    )
).download(SEED_URL)
