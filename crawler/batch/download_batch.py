import tempfile
from ..application.usecase import DownloadHtmlUsecase


class DownloadBatch:

    def __init__(self, usecase: DownloadHtmlUsecase):
        self.usecase = usecase

    def download(self, seed_url: str) -> None:
        """
        SEED_URLからダウンロードを開始します。

        :param seed_url:
        :return:
        """
        if self._is_other_batch_running():
            return

        self.start()
        try:
            self.usecase.download(seed_url)
        except Exception:
            print("エラーが発生しました.")
        finally:
            self.end()

    def _is_other_batch_running(self) -> bool:
        pass

    def start(self) -> None:
        print(tempfile.gettempdir())

    def end(self) -> None:
        pass
