from enum import Enum

from .common import Component
from .collection import Collection as Header, Collection as Footer
from .components import (
    Button,
    Image,
    Link,
    Otp,
    Socials,
    Text,
    ViewInBrowser,
    QrCode,
    StoreBadges,
    Signature,
    SignatureFont,
)


class Theme(Enum):
    UNSTYLED = "UNSTYLED"
    SIMPLE = "SIMPLE"


class Content:
    def __init__(self):
        self.version = 0
        self._theme = Theme.UNSTYLED
        self._header = []
        self.body = [[]]
        self._footer = []

    def theme(self, theme: Theme):
        self._theme = theme
        return self

    def header(self, header: Header):
        self._header = header.components
        return self

    def footer(self, footer: Footer):
        self._footer = footer.components
        return self

    def button(self, text: str, url: str):
        return self.push(Button(text, url))

    def image(
        self,
        src: str,
        url: str = None,
        width: int = None,
        height: int = None,
        alt: str = None,
    ):
        return self.push(Image(src, alt, width, height, url))

    def link(self, text: str, url: str):
        return self.push(Link(text, url))

    def otp(self, text: str):
        return self.push(Otp(text, text))

    def socials(self, data):
        return self.push(Socials(data))

    def text(self, text: str):
        return self.push(Text(text))

    def view_in_browser(self, text: str = None):
        return self.push(ViewInBrowser(text))

    def qr_code(self, url: str):
        return self.push(QrCode.url(url))

    def store_badges(self, data):
        return self.push(StoreBadges(data))

    def signature(self, text: str, font: SignatureFont = None):
        return self.push(Signature(text, font))

    def component(self, c):
        return self.push(c)

    def push(self, component: Component):
        self.body[0].append(component)
        return self

    def build(self):
        return self

    def to_dict(self) -> dict:
        return {
            "version": self.version,
            "theme": self._theme.value,
            "header": [component.to_dict() for component in self._header],
            "body": [[component.to_dict() for component in row] for row in self.body],
            "footer": [component.to_dict() for component in self._footer],
        }
