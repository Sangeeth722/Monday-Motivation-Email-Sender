
import smtplib
import datetime as dt
import random

my_email = "yor email id"
password = "app password "

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 0:
    with open("quotes.txt",mode= "r") as file:
        all_quotes = file.readlines() #convert to list
        quote = random.choice(all_quotes)


    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,to_addrs="to1@gmail.com",msg=f"Subject:Motivation Quotes \n\n {quote}")




