import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
load_dotenv()

URL = os.getenv("URL")

headers = {
    'content-type': 'text/html;charset=UTF-8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
}


def price_tracker():

    res = requests.get(URL, headers=headers)

    soup = BeautifulSoup(res.content, 'html.parser')

    print('product_title -', soup.find('span', id='productTitle').text.strip())
    print('product_price -', soup.find('span',
                                       id='priceblock_ourprice').text.strip())


price_tracker()
