import abc

from ..model.page import Page
from ..model.url import URL


class WebService(abc.ABC):

    @abc.abstractmethod
    def fetch(self, url: URL) -> Page:
        """
        URL指定でページを取得する

        ビジネスルール
         1. 間隔を設ける: 少なくとも1秒は間隔を空けるようにする。
         2. タイムアウトを設定する: サイトの応答が著しく悪い場合があります。そのような場合は、タイムアウトを設定しましょう。
         3. リトライをする: 普段のサイトの応答が悪くなくとも、タイミングによってはエラーが返されることがあります。なるべくクロール時に同時性を持ったデータを収集したい場合は、リトライする仕組みを入れると良いでしょう。

        :param url:
        :return:
        """
        pass
