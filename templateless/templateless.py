import requests

from .errors import (
    UnavailableError,
    UnknownError,
    UnauthorizedError,
    ForbiddenError,
    BadRequestError,
    BadRequestCode,
    InvalidParameterError,
)
from .email import Email


class EmailResponse:
    def __init__(self, emails):
        self.emails = emails


class Templateless:
    def __init__(self, api_key):
        self.api_key = api_key
        self.domain = "https://api.templateless.com"

    def domain(self, domain):
        self.domain = domain
        return self

    def send(self, email: Email):
        return self.send_many([email])

    def send_many(self, emails: list[Email]):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Referer": "templateless-python v0.1.0",
        }

        payload = [email.to_dict() for email in emails]
        response = requests.post(
            f"{self.domain}/v1/emails", headers=headers, json={"payload": payload}
        )

        if response.status_code == 401:
            raise UnauthorizedError
        elif response.status_code == 403:
            raise ForbiddenError
        elif response.status_code == 422:
            error_detail = response.json()
            raise InvalidParameterError(error_detail.get("field", ""))
        elif response.status_code == 400:
            error_detail = response.json()
            raise BadRequestError(
                error_detail.get("code", BadRequestCode.EmailNoContent),
                error_detail.get("error", ""),
            )
        elif response.status_code == 500:
            raise UnavailableError
        elif response.status_code == 200:
            emails_response = EmailResponse(emails=response.json().get("emails", []))
            return emails_response.emails
        else:
            raise UnknownError
