from .components import Button, Image, Link, Otp, Socials, Text, ViewInBrowser


class Collection:
    def __init__(self):
        self.components = []

    def button(self, text, url):
        self.components.append(Button(text, url))
        return self

    def image(self, src, url=None, width=None, height=None, alt=None):
        self.components.append(Image(src, url, width, height, alt))
        return self

    def link(self, text, url):
        self.components.append(Link(text, url))
        return self

    def otp(self, text):
        self.components.append(Otp(text))
        return self

    def socials(self, data):
        self.components.append(Socials(data))
        return self

    def text(self, text):
        self.components.append(Text(text))
        return self

    def view_in_browser(self, text):
        self.components.append(ViewInBrowser(text))
        return self

    def build(self):
        return self
