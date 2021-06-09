import random
import datetime
import smtplib

MY_EMAIL = "shumingting0@gmail.com"
MY_PASSWORD = "Star0258"

now_week = datetime.datetime.now().weekday()
if now_week == 0:
    with open("quotes.txt") as file:
        content = file.readlines()
        print(content)
        quote = random.choice(content)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="hifuggy@yahoo.com",
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )
