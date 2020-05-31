import re
from urllib.parse import urlparse
from dataclasses import dataclass


@dataclass(init=False, frozen=True)
class URL:
    absolute_path: str

    def __init__(self, absolute_path: str):
        assert absolute_path is not None, \
            "Noneが指定されています。絶対パスを指定してください。"
        assert self._is_absolute_path(absolute_path), \
            "{}は絶対パスではありません。絶対パスを指定してください。".format(absolute_path)
        super().__setattr__("absolute_path", absolute_path)

    @staticmethod
    def of(path: str, from_url):
        assert path is not None, "Noneが指定されています。絶対パスを指定してください。"

        if URL._is_absolute_path(path):
            return URL(path)

        _from = urlparse(from_url.absolute_path)
        return URL(_from.scheme + "://" + _from.netloc + "/" + path)

    def match(self, regex: str) -> bool:
        return re.match(regex, self.absolute_path) is not None

    @staticmethod
    def _is_absolute_path(path: str) -> bool:
        return re.match(r"^https?://[\w/:%#\$&\?\(\)~\.=\+\-]+", path) is not None
