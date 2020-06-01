import time
import requests
import datetime

from ....domain.model.page import HttpStatus, Page, URL
from ....domain.model.page.html import CharacterCode, Html
from ....domain.service.web_service import WebService


class SyncWebService(WebService):

    def fetch(self, url: URL) -> Page:
        try:
            response = requests.get(url.absolute_path, timeout=(3.0, 3.0))
            time.sleep(1)
        except:
            return Page(
                url, Html('', CharacterCode.UTF_8),
                HttpStatus.REQUEST_TIMEOUT, datetime.datetime.now()
            )

        return Page(
            url,
            Html(
                response.text,
                CharacterCode.value_of(response.encoding)
            ),
            HttpStatus(response.status_code),
            datetime.datetime.now()
        )
