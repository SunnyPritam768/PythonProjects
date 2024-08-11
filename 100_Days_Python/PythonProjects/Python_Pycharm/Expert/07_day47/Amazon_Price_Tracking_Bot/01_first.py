from bs4 import BeautifulSoup
import requests
import smtplib

MY_Email = "pythonmail45@gmail.com"
MY_Password = "gdnwapftbipsnxek"
Sender_Mail = "sunnypritam2003@gmail.com"
URL = "https://appbrewery.github.io/instant_pot/"
response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
price = soup.find(name="span", class_="a-price-whole")

if price:
    get_price = price.getText().replace(",", "").strip()  # Remove commas and strip spaces
    try:
        floated_price = float(get_price)
        print(floated_price)
    except ValueError:
        print("Error: Could not convert price to float.")
else:
    print("Error: Price not found.")

Buy_Price = 100
title = soup.find(id="productTitle").getText().strip() if soup.find(id="productTitle") else "No title found"
print(title)

if price and floated_price < Buy_Price:
    message = f"{title} is on sale for {floated_price}"

    try:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            result = connection.login(MY_Email, MY_Password)
            connection.sendmail(
                from_addr=MY_Email,
                to_addrs=Sender_Mail,
                msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8")
            )
    except Exception as e:
        print(f"Error: {e}")
else:
    print("No email sent.")
