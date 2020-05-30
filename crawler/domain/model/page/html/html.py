from dataclasses import dataclass

from .character_code import CharacterCode


@dataclass(frozen=True)
class Html:
    text: str
    character_code: CharacterCode
