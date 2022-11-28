import email, smtplib, ssl
from providers import PROVIDERS

def send_sms_via_email(
    number: str,
    message: str,
    provider: str,
    sender_credentials: tuple,
    subject: str = "sent using etext",
    smtp_server: str = "smtp.gmail.com",
    smtp_port: int = 465,
):
    sender_email, email_password = sender_credentials
    receiver_email = f'{number}@{PROVIDERS.get(provider).get("sms")}'

    email_message = f"Subject:{subject}\nTo:{receiver_email}\n{message}"

    with smtplib.SMTP_SSL(
        smtp_server, smtp_port, context=ssl.create_default_context()
    ) as email:
        email.login(sender_email, email_password)
        email.sendmail(sender_email, receiver_email, email_message)




# vunbouvogkeazgxp
def main():
    number = "5186535318"
    message = "hello world!"
    provider = "Verizon"

    # CHANGE THE PASSWORD AND PHONE SO YOU DON'T DOX YOURSELF
    sender_credentials = ("mp3converterandencryptor@gmail.com", "vunbouvogkeazgxp")

    send_sms_via_email(number, message, provider, sender_credentials)


if __name__ == "__main__":
    main()


# Need to go to  https://myaccount.google.com/apppasswords after setting up 2 factor on your account