from ..common import ComponentId, Component


class ViewInBrowser(Component):
    def __init__(self, text=None):
        self.id = ComponentId.VIEW_IN_BROWSER
        self.text = text

    def to_dict(self) -> dict:
        return {
            "id": self.id.value,
            "text": self.text,
        }
