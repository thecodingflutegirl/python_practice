import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
import os

AMAZON_URL = 'https://www.amazon.com/Urban-CoCo-Womens-Vintage-Stretchy/dp/B01N5LP929/ref=sr_1_1_sspa?crid=19KRPD3DWDLJL&keywords=Urban%2BCoCo%2BWomen%27s%2BVintage%2BVelvet%2BStretchy%2BMini%2BFlared%2BSkater%2BSkirt&qid=1641583161&sprefix=urban%2Bcoco%2Bwomen%27s%2Bvintage%2Bvelvet%2Bstretchy%2Bmini%2Bflared%2Bskater%2Bskirt%2Caps%2C72&sr=8-1-spons&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyUkpYN1BLNFZEWU1YJmVuY3J5cHRlZElkPUEwMzMxMDY4M0E2TjFHWkQ5WU1SMiZlbmNyeXB0ZWRBZElkPUEwMjIwMDY3MktYRFA1NVBWVUZMTiZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU&th=1&psc=1'

BUY_PRICE = 20
my_email = os.environ['MY_EMAIL']
password = os.environ['EMAIL_PASSWORD']

headers = {
    'Accept-Language': 'en-US,en;q=0.9',
    'User-Agent': 'Defined'
}

response = requests.get(AMAZON_URL, headers=headers)
response.raise_for_status()
amazon_page = response.content

soup = BeautifulSoup(amazon_page, 'lxml')
price = soup.find(name='span', class_=[
                  'a-offscreen', 'apexPriceToPay']).get_text()
price_number = float(price.split('$')[1])
formatted_price = "{:.2f}".format(price_number)
# print(price_number)
name_of_product = soup.find(name='span', id='productTitle').get_text()
# print(name_of_product)

if price_number < BUY_PRICE:
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            to_addrs=my_email, from_addr=my_email, msg=f"Subject:Amazon Price Alert!\n\n{name_of_product} is now only ${formatted_price}. Click the link to view: \n{AMAZON_URL}")
