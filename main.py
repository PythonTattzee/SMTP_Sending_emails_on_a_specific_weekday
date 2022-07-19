import datetime as dt
import random
import smtplib
import calendar

DAY_OF_SENDING = 2
# here I define the sender email and password that I will use later.
my_email = "test977657576@outlook.com"
password = "DSkgjd93958%50"

# here I define the day of the week on which I will send the email
now = dt.datetime.now()
day_of_week = now.weekday()
print(day_of_week)

#I put this function first and later I execute it in the if statement.
def send_email():
    #I connect to the corresponding email server
    with smtplib.SMTP("outlook.office365.com") as connection:
        #secure the connection
        connection.starttls()
        #login to the service
        connection.login(user=my_email, password=password)
        #and finally send the email
        connection.sendmail(from_addr=my_email, to_addrs="dxbb2456@yahoo.com", msg=f"Subject: Motivational quote\n\n{quote}")


# here I read and convert the data file to a list.
with open("quotes.txt", "r") as data:
    data_list = data.readlines()
    quote = random.choice(data_list)
# if the day of the week equal to the day when
# the message should be sent then send the message
if day_of_week == DAY_OF_SENDING:
    send_email()


print(quote)
