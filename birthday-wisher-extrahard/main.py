import random
import smtplib
import pandas
import datetime

MY_EMAIL = "shumingting0@gmail.com"
MY_PASSWORD = "Star0258"

data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in data.iterrows()}

today = datetime.datetime.now()
today_tuple = (today.month, today.day)

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as file:
        content = file.read()
        new_letter = content.replace("[NAME]", birthday_person['name'])
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=birthday_person["email"],
                msg=f"Subject:Happy Birthday!!!\n\n{new_letter}"
            )
