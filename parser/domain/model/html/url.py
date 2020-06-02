import re
from dataclasses import dataclass


@dataclass(init=False, unsafe_hash=True, frozen=True)
class URL:
    absolute_path: str

    def __init__(self, absolute_path: str):
        assert absolute_path is not None, \
            "Noneが指定されています。絶対パスを指定してください。"
        assert self._is_absolute_path(absolute_path), \
            "{}は絶対パスではありません。絶対パスを指定してください。".format(absolute_path)
        super().__setattr__("absolute_path", absolute_path)

    @staticmethod
    def _is_absolute_path(path: str) -> bool:
        return re.match(r"^https?://[\w/:%#\$&\?\(\)~\.=\+\-]+", path) is not None
