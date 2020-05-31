import requests
import datetime

from ....domain.model.page import HttpStatus, Page
from ....domain.model.page.html import CharacterCode, Html
from ....domain.model.url import URL
from ....domain.service.web_service import WebService


class SyncWebService(WebService):

    def fetch(self, url: URL) -> Page:
        response = requests.get(url.absolute_path)

        return Page(
            url,
            Html(
                response.text,
                CharacterCode.value_of(response.encoding)
            ),
            HttpStatus(response.status_code),
            datetime.datetime.now()
        )
