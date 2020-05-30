from typing import List


class RequestAPIUsecase:
    def __init__(self):
        self.api_service = None
        self.json_repository = None

    def request(self, urls: List[str]):
        for url in urls:
            response = self.api_service.request(url)
            if response.is_ok:
                self.json_repository.save(response)
