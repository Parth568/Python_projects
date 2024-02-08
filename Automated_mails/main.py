import smtplib
import datetime as dt
import random

My_email = "pyparth2@gmail.com"
password = "jzqyjyeacsozualt"
receiver_mail = "cparth6543@gmail.com"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 3:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(My_email, password)
        connection.sendmail(from_addr=My_email,
                            to_addrs=receiver_mail,
                            msg=f"Subject: Thursday Motivation\n\n{quote}"
                            )
