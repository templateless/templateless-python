from ..common import ComponentId, Component


class Image(Component):
    def __init__(self, src, alt, width, height, url):
        self.id = ComponentId.IMAGE
        self.src = src
        self.alt = alt
        self.width = width
        self.height = height
        self.url = url

    def to_dict(self):
        return {
            "id": self.id.value,
            "src": self.src,
            "alt": self.alt,
            "width": self.width,
            "height": self.height,
            "url": self.url,
        }
