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


class Item:
    def __init__(self, service: Service, value: str):
        self.service = service
        self.value = value

    def serialize_item(item):
        return {"service": item.service.value, "value": item.value}


class Socials(Component):
    def __init__(self, data):
        self.id = ComponentId.SOCIALS
        self.data = data

    def serialize_socials(socials):
        return {"id": socials.id.value, "data": [item for item in socials.data]}
