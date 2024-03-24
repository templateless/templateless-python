from ..common import ComponentId, Component


class Image(Component):
    def __init__(self, src, url=None, width=None, height=None, alt=None):
        self.id = ComponentId.IMAGE
        self.src = src
        self.alt = alt
        self.width = width
        self.height = height
        self.url = url

    def to_dict(self) -> dict:
        attributes = {
            "id": self.id.value,
            "src": self.src,
            "alt": self.alt,
            "width": self.width,
            "height": self.height,
            "url": self.url,
        }
        return {key: value for key, value in attributes.items() if value is not None}
