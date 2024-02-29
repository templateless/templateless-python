import os
import sys
from dotenv import load_dotenv
from templateless import (
    Content,
    Email,
    EmailAddress,
    Templateless,
    Header,
    SocialItem,
    Service,
    Footer,
)


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

    header = Header().text("# ExampleApp").build()

    footer = (
        Footer()
        .socials(
            [
                SocialItem(Service.TWITTER, "ExampleApp"),
                SocialItem(Service.GITHUB, "ExampleApp"),
            ]
        )
        .link("Unsubscribe", "https://example.com/unsubscribe?id=123")
        .build()
    )

    content = Content().header(header).text("Hello world").footer(footer).build()

    email = (
        Email()
        .to(EmailAddress(email_address))
        .subject("Confirm your email")
        .content(content)
        .build()
    )

    templateless = Templateless(api_key)
    result = templateless.send(email)

    print(result)


if __name__ == "__main__":
    main()
