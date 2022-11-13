import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_html(url):
    r = requests.get(url)
    return r.text

def webparsing(html):
    result = pd.DataFrame(columns=['Names', 'Price'])

    soup = BeautifulSoup(html, features="html.parser")

    names = []
    prices = []


    for item in soup.find_all("div", class_="info"):
        name_str = item.find("h3", class_="title")
        price_str = item.find("div", class_="price").find("div").text
        names.append(name_str.text)
        prices.append(price_str)




url_list = ['https://www.lcwaikiki.kz/ru-RU/KZ/tag/men-outerwear?PageIndex=1',
            'https://www.lcwaikiki.kz/ru-RU/KZ/tag/men-outerwear?PageIndex=2',
            'https://www.lcwaikiki.kz/ru-RU/KZ/tag/men-outerwear?PageIndex=3',
            'https://www.lcwaikiki.kz/ru-RU/KZ/tag/men-outerwear?PageIndex=4',
            'https://www.lcwaikiki.kz/ru-RU/KZ/tag/men-outerwear?PageIndex=5'
]

for url in url_list:
    webparsing(get_html(url))