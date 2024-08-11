# How to send message from one user to another through mail
import smtplib

my_email = "pythonmail45@gmail.com"
password = "gdnwapftbipsnxek"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="udemyuser@yahoo.com",
        msg="Subject: Hello\n\nThis is the BODY of my email"
    )
