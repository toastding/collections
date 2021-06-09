import random
import smtplib

import pandas
import datetime

MY_EMAIL = "shumingting0@gmail.com"
MY_PASSWORD = "Star0258"
PLACEHOLDER = "[NAME]"
# random letter
letter = random.randint(1, 4)

# whose birthday
data = pandas.read_csv("birthdays.csv")
birth = data.to_dict(orient='records')

# today
now = datetime.datetime.now()
month = now.month
day = now.day

# Check if today matches a birthday in the birthdays.csv
for i in range(len(birth)):
    if birth[i]['month'] == month and birth[i]['day'] == day:
        print(birth[i])
        # pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        with open(f"letter_templates/letter_{letter}.txt") as file:
            content = file.read()
            new_letter = content.replace(PLACEHOLDER, birth[i]['name'])
            # Send the letter generated in step 3 to that person's email address.
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=MY_PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=birth[i]["email"],
                    msg=f"Subject:Happy Birthday!!!\n\n{new_letter}"
                )
