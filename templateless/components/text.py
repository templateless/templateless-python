from ..common import ComponentId, Component


class Text(Component):
    def __init__(self, text):
        self.id = ComponentId.TEXT
        self.text = text

    def to_dict(self):
        return {
            "id": self.id.value,
            "text": self.text,
        }
