from bs4 import BeautifulSoup
import requests
import lxml
import smtplib

MY_EMAIL = "shumingting0@gmail.com"
MY_PASSWORD = "Aq3670oo"

headers = {
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "ja-JP,ja;q=0.9,zh-TW;q=0.8,zh;q=0.7,en;q=0.6",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36",
}

url = "https://www.amazon.com/-/zh_TW/CRKT-Drifter-EDC-%E6%8A%98%E7%96%8A%E5%8F%A3%E8%A2%8B%E5%88%80-%E6%8B%87%E6%8C%87%E8%9E%BA%E6%9F%B1%E9%96%8B%E5%8F%A3/dp/B001DZMBY4/ref=sr_1_41?crid=3H2C0WD176CXL&dchild=1&keywords=pocket+knife&qid=1627525148&sprefix=pocket%2Caps%2C421&sr=8-41"

response = requests.get(url=url, headers=headers)
soup = BeautifulSoup(response.content, "lxml")
price = soup.find(name="span", id="price_inside_buybox").getText()
product = soup.find(name="h4", class_="vse-video-title-text").getText().split(":")[0]

price = price.split("US$")[1][:5]


if float(price) < 50:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="hifuggy@yahoo.com",
            msg=f"Subject:Amazon Price Alert!\n\n{product}\nnow US${price}\n{url}"
        )

