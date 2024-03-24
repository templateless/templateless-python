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
    Theme,
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

    header = (
        Header()
        .image(src="https://templateless.net/myco.webp", width=100, alt="MyCo")
        .build()
    )

    footer = (
        Footer()
        .text(
            "If you did not sign up for a MyCo account, please ignore this email.\nThis link will expire in 24 hours."
        )
        .socials(
            [
                SocialItem(Service.TWITTER, "MyCo"),
                SocialItem(Service.GITHUB, "MyCo"),
            ]
        )
        .link("Unsubscribe", "https://example.com")
        .build()
    )

    verify_email_link = "https://example.com/verify?token=ABC"

    content = (
        Content()
        .theme(Theme.SIMPLE)
        .header(header)
        .text("Hi there,")
        .text(
            "Welcome to **MyCo**! We're excited to have you on board. Before we get started, we need to verify your email address."
        )
        .text("Please confirm your email by clicking the button below:")
        .button("Verify Email", verify_email_link)
        .text("Or use the link below:")
        .link(verify_email_link, verify_email_link)
        .footer(footer)
        .build()
    )

    email = (
        Email()
        .to(EmailAddress(email_address))
        .subject("Confirm your email")
        .content(content)
        .build()
    )

    templateless = Templateless(api_key)
    templateless.send(email)


if __name__ == "__main__":
    main()
