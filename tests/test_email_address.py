from templateless.email_address import EmailAddress


def test_email_address_to_dict():
    email = "example@example.com"
    name = "John Doe"
    email_address = EmailAddress(email=email, name=name)

    result = email_address.to_dict()

    expected = {"email": email, "name": name}

    assert result == expected, "EmailAddress to_dict does not match expected dictionary"
