from enum import Enum
from ..common import ComponentId, Component


class Font(Enum):
    REENIE_BEANIE = 1
    MEOW_SCRIPT = 2
    CAVEAT = 3
    ZEYADA = 4
    PETEMOSS = 5


class Signature(Component):
    def __init__(self, text: str, font: Font = None):
        self.id = ComponentId.SIGNATURE
        self.text = text
        self.font = font

    def to_dict(self) -> dict:
        return {
            "id": self.id.value,
            "text": self.text,
            "font": self.font.name if self.font else None,
        }
