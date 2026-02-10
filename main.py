# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import pandas as pd
import datetime as dt
import smtplib
import random
import os

data = pd.read_csv('birthdays.csv')
cur_time = dt.datetime.now()
letter = ""
letters = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]
email = ""

username = os.environ.get("MY_EMAIL")
password = os.environ.get("MY_PASSWORD)

for i in range(data["name"].size):
    if (data["day"][i] == cur_time.day and
        data["month"][i] == cur_time.month
        ):
        email = data["email"][i]
        with open(random.choice(letters), "r") as letter_file:
            letter = letter_file.read()
            letter = letter.replace("[NAME]", data["name"][i])
            print(letter)
if not letter:
    quit()
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(username, password)
    connection.sendmail(
        from_addr=username,
        to_addrs=email,
        msg=f"Subject: Happy Birthday!\n\n{letter}"
    )


