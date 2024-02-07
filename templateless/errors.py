class BadRequestCode:
    ACCOUNT_QUOTA_EXCEEDED = 200
    PROVIDER_KEY_MISSING = 300
    PROVIDER_KEY_INVALID = 301
    EMAIL_NO_CONTENT = 400

    @staticmethod
    def error_message(code):
        messages = {
            BadRequestCode.ACCOUNT_QUOTA_EXCEEDED: "account quota exceeded",
            BadRequestCode.PROVIDER_KEY_MISSING: "provider key missing",
            BadRequestCode.PROVIDER_KEY_INVALID: "provider key invalid",
            BadRequestCode.EMAIL_NO_CONTENT: "email has no content to send",
        }
        return messages.get(code, "Unknown error code")


class Error(Exception):
    pass


class UnauthorizedError(Error):
    pass


class ForbiddenError(Error):
    pass


class InvalidParameterError(Error):
    def __init__(self, field):
        self.field = field


class BadRequestError(Error):
    def __init__(self, code, error):
        self.code = code
        self.error = error


class UnavailableError(Error):
    pass


class UnknownError(Error):
    pass
