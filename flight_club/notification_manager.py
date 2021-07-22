import smtplib
from twilio.rest import Client

TWILIO_SID = "ACe1ae4e388a1a7390b292e744d125d13f"
TWILIO_AUTH_TOKEN = "36149300860710b127c0a038229f2eeb"
TWILIO_VIRTUAL_NUMBER = '+17742284856'
TWILIO_VERIFIED_NUMBER = '+886978199305'
MAIL_PROVIDER_SMTP_ADDRESS = "hifuggy@yahoo.com"
MY_EMAIL = "shumingting0@gmail.com"
MY_PASSWORD = "Star0258"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )