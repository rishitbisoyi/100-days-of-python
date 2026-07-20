from bs4 import BeautifulSoup
import requests
import smtplib

URL = "AMAZON_PRODUCT_URL"

MY_EMAIL = "email@gmail.com"
PASSWORD = "app_password"

BUY_PRICE = 100

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:139.0) Gecko/20100101 Firefox/139.0",
    "Accept-Language": "en-US,en;q=0.9",
}

response = requests.get(URL, headers=headers)
response.raise_for_status()

soup = BeautifulSoup(response.text, "lxml")

title = soup.find(id="productTitle").get_text().strip()

price = float(
    soup.find(class_="a-offscreen")
    .get_text()
    .replace("$", "")
    .replace("₹", "")
    .replace(",", "")
)

print(title)
print(price)

if price <= BUY_PRICE:
    message = f"{title}\n\nNow only ₹{price}\n{URL}"

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(
            user=MY_EMAIL,
            password=PASSWORD
        )

        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}".encode("utf-8")
        )

    print("Email sent!")
else:
    print("Price is still above your target price.")