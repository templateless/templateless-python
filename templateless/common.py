from enum import Enum


class ComponentId(Enum):
    BUTTON = "BUTTON"
    IMAGE = "IMAGE"
    LINK = "LINK"
    OTP = "OTP"
    POWERED_BY = "POWERED_BY"
    SOCIALS = "SOCIALS"
    TEXT = "TEXT"
    VIEW_IN_BROWSER = "VIEW_IN_BROWSER"
    QR_CODE = "QR_CODE"
    SIGNATURE = "SIGNATURE"
    STORE_BADGES = "STORE_BADGES"


class Component:
    pass
