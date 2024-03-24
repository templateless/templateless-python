from enum import Enum
from ..common import ComponentId, Component


class Service(Enum):
    WEBSITE = "WEBSITE"
    EMAIL = "EMAIL"
    PHONE = "PHONE"
    FACEBOOK = "FACEBOOK"
    YOUTUBE = "YOUTUBE"
    TWITTER = "TWITTER"
    X = "X"
    GITHUB = "GITHUB"
    INSTAGRAM = "INSTAGRAM"
    LINKEDIN = "LINKEDIN"
    SLACK = "SLACK"
    DISCORD = "DISCORD"
    TIKTOK = "TIKTOK"
    SNAPCHAT = "SNAPCHAT"
    THREADS = "THREADS"
    TELEGRAM = "TELEGRAM"
    MASTODON = "MASTODON"
    RSS = "RSS"


class Item:
    def __init__(self, service: Service, value: str):
        self.service = service
        self.value = value

    def to_dict(self) -> dict:
        return {"key": self.service.value, "value": self.value}


class Socials(Component):
    def __init__(self, data):
        self.id = ComponentId.SOCIALS
        self.data = data

    def to_dict(self) -> dict:
        return {"id": self.id.value, "data": [item.to_dict() for item in self.data]}
