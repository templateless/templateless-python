from ..common import ComponentId, Component


class Otp(Component):
    def __init__(self, text):
        self.id = ComponentId.OTP
        self.text = text

    def to_dict(self):
        return {
            "id": self.id.value,
            "text": self.text,
        }
