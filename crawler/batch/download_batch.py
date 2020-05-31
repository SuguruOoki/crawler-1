import os
from tempfile import gettempdir

from ..application.usecase import DownloadHtmlUsecase


class DownloadBatch:

    def __init__(self, usecase: DownloadHtmlUsecase, batch_name: str):
        self.usecase = usecase
        self.batch_name = batch_name

    def download(self, seed_url: str) -> None:
        """
        SEED_URLからダウンロードを開始します。

        :param seed_url:
        :return:
        """
        if self._is_other_batch_running():
            print("他のバッチが起動中です.プログラムを終了します.")
            return

        self._create_pid_file()
        try:
            print("クロールを開始します.")
            self.usecase.download(seed_url)
        finally:
            self._rm_pid_file()
            print("クロールを終了します.")

    def _is_other_batch_running(self) -> bool:
        return os.path.exists(self._pid_path())

    def _create_pid_file(self) -> None:
        with open(self._pid_path(), "w") as p:
            p.write(str(os.getpid()))

    def _rm_pid_file(self) -> None:
        os.remove(self._pid_path())

    def _pid_path(self) -> str:
        return os.path.join(gettempdir(), self.batch_name + ".pid")
