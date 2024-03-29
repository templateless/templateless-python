import os
import sys
from dotenv import load_dotenv
from templateless import Content, Email, EmailAddress, Templateless


def main():
    load_dotenv()

    api_key = os.getenv("TEMPLATELESS_API_KEY")
    if api_key is None:
        print("Set TEMPLATELESS_API_KEY to your Templateless API key")
        sys.exit(1)

    email_address = os.getenv("TEMPLATELESS_EMAIL_ADDRESS")
    if email_address is None:
        print("Set TEMPLATELESS_EMAIL_ADDRESS to your own email address")
        sys.exit(1)

    email = (
        Email()
        .to(EmailAddress(email_address))
        .subject("Hello 👋")
        .content(Content().text("Hello world").build())
        .build()
    )

    templateless = Templateless(api_key)
    templateless.send(email)


if __name__ == "__main__":
    main()
