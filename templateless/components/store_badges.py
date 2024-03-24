from enum import Enum
from typing import List
from ..common import ComponentId, Component


class StoreBadge(Enum):
    APP_STORE = "APP_STORE"
    GOOGLE_PLAY = "GOOGLE_PLAY"
    MICROSOFT_STORE = "MICROSOFT_STORE"


class Item:
    def __init__(self, key: StoreBadge, value: str):
        self.key = key
        self.value = value

    def to_dict(self):
        return {"key": self.key.value, "value": self.value}


class StoreBadges(Component):
    def __init__(self, data: List[Item]):
        self.id = ComponentId.STORE_BADGES
        self.data = data

    def to_dict(self):
        return {"id": self.id.value, "data": [item.to_dict() for item in self.data]}
