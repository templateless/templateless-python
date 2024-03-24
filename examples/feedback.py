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
        .socials(
            [
                SocialItem(Service.TWITTER, "MyCo"),
                SocialItem(Service.GITHUB, "MyCo"),
            ]
        )
        .build()
    )

    content = (
        Content()
        .theme(Theme.SIMPLE)
        .header(header)
        .text("Hey Alex,")
        .text("I'm Jamie, founder of **MyCo**.")
        .text(
            "Could you spare a moment to reply to this email with your thoughts on our service? Your feedback is invaluable and directly influences our improvements."
        )
        .text(
            "When you hit reply, your email will go directly to me, and I read each and every one."
        )
        .text("Thanks for your support,")
        .signature("Jamie Parker")
        .text("Jamie Parker\n\nFounder @ [MyCo](https://example.com)")
        .footer(footer)
        .build()
    )

    email = (
        Email()
        .to(EmailAddress(email_address))
        .subject("Thoughts on service?")
        .content(content)
        .build()
    )

    templateless = Templateless(api_key)
    templateless.send(email)


if __name__ == "__main__":
    main()
