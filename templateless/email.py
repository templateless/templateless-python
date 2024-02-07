from .content import Content


class EmailOptions:
    def __init__(self, delete_after=None):
        self.delete_after = delete_after


class Email:
    def __init__(self):
        self._to = set()
        self._subject = ""
        self._content = Content()
        self.options = EmailOptions()

    def to(self, email_address):
        self._to.add(email_address)
        return self

    def to_many(self, email_addresses):
        self._to.update(email_addresses)
        return self

    def subject(self, subject):
        self._subject = subject
        return self

    def content(self, content):
        self._content = content
        return self

    def delete_after(self, seconds):
        self.options.delete_after = seconds
        return self

    def build(self):
        return self

    def to_dict(self):
        return {
            "to": [to.to_dict() for to in self._to],
            "subject": self._subject,
            "content": self._content.to_dict()
            if hasattr(self._content, "to_dict")
            else self._content,
            "options": {"delete_after": self.options.delete_after},
        }
