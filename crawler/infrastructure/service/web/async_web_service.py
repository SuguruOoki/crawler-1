from ....domain.model.page import Page
from ....domain.model.url import URL
from ....domain.service.web_service import WebService


class AsyncWebService(WebService):

    def fetch(self, url: URL) -> Page:
        pass
