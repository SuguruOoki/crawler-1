from enum import Enum


class CharacterCode(Enum):
    UTF_8 = 1
    SHIFT_JIS = 2

    @staticmethod
    def value_of(char_code: str):
        if (char_code == "UTF-8") or (char_code == "utf-8"):
            return CharacterCode.UTF_8
        elif (char_code == "SHIFT-JIS") or (char_code == "shift-jis"):
            return CharacterCode.SHIFT_JIS
        else:
            raise Exception("該当の文字コードが存在しません。 (文字コード = {})".format(char_code))
