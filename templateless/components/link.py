from ..common import ComponentId, Component


class Link(Component):
    def __init__(self, text, url):
        self.id = ComponentId.LINK
        self.text = text
        self.url = url

    def to_dict(self):
        return {
            "id": self.id.value,
            "text": self.text,
            "url": self.url,
        }
