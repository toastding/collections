import smtplib

my_email = "shumingting0@gmail.com"
password = "Star0258"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="hifuggy@yahoo.com",
        msg="Subject:Hello\n\nThis is the body of my email"
    )

