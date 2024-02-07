from ..common import ComponentId, Component


class Button(Component):
    def __init__(self, text: str, url: str):
        self.id = ComponentId.BUTTON
        self.text = text
        self.url = url

    def to_dict(self):
        return {"id": self.id.value, "text": self.text, "url": self.url}
