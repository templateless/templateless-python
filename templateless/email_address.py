class EmailAddress:
    def __init__(self, email, name=None):
        self.email = email
        self.name = name

    def to_dict(self) -> dict:
        return {"email": self.email, "name": self.name}
