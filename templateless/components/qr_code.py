import base64
from enum import Enum
from ..common import ComponentId, Component


class Cryptocurrency(Enum):
    BITCOIN = "bitcoin"
    ETHEREUM = "ethereum"


class QrCode(Component):
    def __init__(self, data: str):
        self.id = ComponentId.QR_CODE
        self.data = data

    @classmethod
    def new(cls, data: bytes) -> "QrCode":
        encoded_data = base64.standard_b64encode(data).decode("utf-8")
        return cls(encoded_data)

    @classmethod
    def email(cls, email: str) -> "QrCode":
        return cls.new(f"mailto:{email}".encode("utf-8"))

    @classmethod
    def url(cls, url: str) -> "QrCode":
        return cls.new(url.encode("utf-8"))

    @classmethod
    def phone(cls, phone: str) -> "QrCode":
        return cls.new(f"tel:{phone}".encode("utf-8"))

    @classmethod
    def sms(cls, text: str) -> "QrCode":
        return cls.new(f"smsto:{text}".encode("utf-8"))

    @classmethod
    def coordinates(cls, lat: float, lng: float) -> "QrCode":
        return cls.new(f"geo:{lat},{lng}".encode("utf-8"))

    @classmethod
    def cryptocurrency_address(
        cls, cryptocurrency: Cryptocurrency, address: str
    ) -> "QrCode":
        return cls.new(f"{cryptocurrency.value}:{address}".encode("utf-8"))

    def to_dict(self) -> dict:
        return {"id": self.id.value, "data": self.data}
