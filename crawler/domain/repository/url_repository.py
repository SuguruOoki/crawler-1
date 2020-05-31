import abc
import datetime

from crawler.domain.model.url import URL, URLSet


class UrlRepository(abc.ABC):

    @abc.abstractmethod
    def has_urls(self) -> bool:
        """
        クロールすべきURLかどうかを判定します。
        クロールすべきURLがある場合、Trueを返します。

        クロールすべきURLとは
         - クロールしたことがないURL
         - 更新する必要があるページのURL

        :return: bool
        """
        raise NotImplementedError("infrastructureパッケージで実装してください")

    @abc.abstractmethod
    def get(self) -> URL:
        """
        クロールすべきURLを一件取得します。

        クロールすべきURLとは
         - クロールしたことがないURL
         - 更新する必要があるページのURL

        :return: URL
        """
        raise NotImplementedError("infrastructureパッケージで実装してください")

    @abc.abstractmethod
    def save(self, url: URL) -> None:
        """
        URLを保存します。

        :param url:
        :return: None
        """
        raise NotImplementedError("infrastructureパッケージで実装してください")

    @abc.abstractmethod
    def crawled(self, url: URL) -> None:
        """
        URLをクローズ済みとして保存します。

        :param url:
        :return: None
        """
        raise NotImplementedError("infrastructureパッケージで実装してください")
