from ....domain.model.page import Page, URL
from ....domain.service.web_service import WebService


class AsyncWebService(WebService):

    def fetch(self, url: URL) -> Page:
        pass
