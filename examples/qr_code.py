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
    StoreBadgeItem,
    StoreBadge,
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

    app_store_link = "https://apps.apple.com/us/app/example/id1234567890"
    google_play_link = "https://play.google.com/store/apps/details?id=com.example"

    footer = (
        Footer()
        .store_badges(
            [
                StoreBadgeItem(StoreBadge.APP_STORE, app_store_link),
                StoreBadgeItem(StoreBadge.GOOGLE_PLAY, google_play_link),
            ]
        )
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
        .text(
            "Thank you for choosing MyCo! To get started with our mobile experience, simply pair your account with our mobile app."
        )
        .text("Here's how to do it:")
        .text(
            "\n".join(
                [
                    f"1. Download the MyCo app from the [App Store]({app_store_link}) or [Google Play]({google_play_link}).",
                    "1. Open the app and select _Pair Device_.",
                    "1. Scan the QR code below with your mobile device:",
                ]
            )
        )
        .qr_code("https://example.com/qr-code-link")
        .text("Enjoy your seamless experience across devices!")
        .footer(footer)
        .build()
    )

    email = (
        Email()
        .to(EmailAddress(email_address))
        .subject("How to Pair Device")
        .content(content)
        .build()
    )

    templateless = Templateless(api_key)
    templateless.send(email)


if __name__ == "__main__":
    main()
