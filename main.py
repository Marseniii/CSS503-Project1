from bs4 import BeautifulSoup
import pandas as pd
import re
import math

html_list = [
    'LC-1.html',
    'LC-2.html',
    'LC-3.html',
    'LC-4.html',
    'LC-5.html',
    'Zara1.html',
    'Zara2.html',
    'Zara3.html',
    'DF1.html',
    'DF2.html',
    'DF3.html',
    'Ostin1.html',
    'Ostin2.html',
    'Ostin3.html',
    'Ostin4.html',
    'NYer.html',
    'Glasman1.html',
    'Glasman2.html',
    'Glasman3.html',
    'Glasman4.html',
    'Glasman5.html',
    'Glasman6.html',
    'SPM1.html',
    'SPM2.html',
    'SPM3.html',
]

names = []
prices = []
discount = []
brand = []
old_price = []
percent = []

for a in html_list:
    with open(a, encoding="utf8") as file:
        src = file.read()

    soup = BeautifulSoup(src, features="html.parser")

    for i in soup.find_all("div", class_="products-list__box-info"):
        name_str = i.find("div", class_="products-list__box-title-short")
        price_str = i.find("div", class_="price-new bigger")
        discount_str = i.find("span", class_="discount")

        names.append(re.sub(' +', ' ', name_str.text.strip()))
        brand.append("Спортмастер")

        price_int = ""
        old_price_int = ""

        if discount_str is None:
            for x in price_str.text:
                if x == ",":
                    break
                if x.isdigit():
                    price_int = price_int + x
            prices.append(price_int.strip())
            old_price.append("-")
            discount.append("No Discount")
            percent.append(0)
        else:
            old_price_str = i.find("div", class_="price-old")
            for x in price_str.text:
                if x == ",":
                    break
                if x.isdigit():
                    price_int = price_int + x
            for y in old_price_str.text:
                if y == ".":
                    break
                if y.isdigit():
                    old_price_int = old_price_int + y
            old_price.append(old_price_int)
            prices.append(price_int.strip())
            discount.append("With Discount")
            percent.append(math.floor((int(old_price_int) - int(price_int)) / int(old_price_int) * 100))

    for i in soup.find_all("div", class_="product"):
        name_str = i.find("div", class_="name").find("a")
        price_str = i.find("div", class_="price")

        price_int = ""

        for x in price_str.text:
            if x == ",":
                break
            if x.isdigit():
                price_int = price_int + x

        names.append(name_str.text)
        prices.append(re.sub(' +', ' ', price_int))
        old_price.append("-")
        brand.append("Glasman")
        discount.append("No Discount")
        percent.append(0)

    for i in soup.find_all("a", class_="_product-item-container_1pvjg_1"):

        name_str = i.find("div", class_="_description_1pvjg_23")
        price_str = i.find("div", class_="_current-price-container_1pvjg_159")
        discount_str = i.find("span", class_="_sale-price_1pvjg_82")

        price_int = ""
        discount_int = ""
        old_price_int = ""

        if discount_str is None:
            if price_str is None:
                pass
            else:
                for x in price_str.text:
                    if x == ".":
                        break
                    if x.isdigit():
                        price_int = price_int + x
                names.append(name_str.text)
                brand.append("New Yorker")
                old_price.append("-")
                prices.append(price_int)
                discount.append("No Discount")
                percent.append(0)
        else:
            old_price_str = i.find("span", class_="_original-price_1pvjg_76")
            for x in discount_str.text:
                if x == ".":
                    break
                if x.isdigit():
                    discount_int = discount_int + x
            for y in old_price_str.text:
                if y == ".":
                    break
                if y.isdigit():
                    old_price_int = old_price_int + y
            names.append(name_str.text)
            brand.append("New Yorker")
            old_price.append(old_price_int)
            prices.append(discount_int)
            discount.append("With Discount")
            percent.append(math.floor((int(old_price_int) - int(discount_int)) / int(old_price_int) * 100))

    for i in soup.find_all("div", class_="product-card__extra"):
        name_str = i.find("div", class_="product-card__name")
        price_str = i.find("div", class_="product-card__price")
        discount_str = i.find("div", class_="product-card__price discount")

        names.append(re.sub(' +', ' ', name_str.text.strip()))
        brand.append("O'Stin")

        price_int = ""
        old_price_int = ""
        discount_int = ""

        if discount_str is None:
            for x in price_str.text:
                if x.isdigit():
                    price_int = price_int + x
            prices.append(price_int.strip())
            discount.append("No Discount")
            old_price.append("-")
            percent.append(0)
        else:
            old_price_str = i.find("div", class_="product-card__price-old")
            for x in discount_str.text:
                if x.isdigit():
                    discount_int = discount_int + x
            for y in old_price_str.text:
                if y.isdigit():
                    old_price_int = old_price_int + y
            prices.append(discount_int.strip())
            discount.append("With Discount")
            old_price.append(re.sub(' +', ' ', old_price_int.strip()))
            percent.append(math.floor((int(old_price_int) - int(discount_int)) / int(old_price_int) * 100))

    for i in soup.find_all("div", class_="product-card__details"):
        name_str = i.find("h3", class_="product-card__title").find("span")
        price_str = i.find("div", class_="product-card__price--new d-inline-flex")
        old_price_str = i.find("div", class_="product-card__price--old d-inline-flex")

        names.append(name_str.text)
        brand.append("DeFacto")

        price_int = ""
        old_price_int = ""

        if old_price_str is None:
            for x in price_str.text:
                if x == ",":
                    break
                if x.isdigit():
                    price_int = price_int + x
            prices.append(re.sub(' +', ' ', price_int))
            discount.append("No Discount")
            old_price.append("-")
            percent.append(0)
        else:
            for x in price_str.text:
                if x == ",":
                    break
                if x.isdigit():
                    price_int = price_int + x
            for y in old_price_str.text:
                if y == ",":
                    break
                if y.isdigit():
                    old_price_int = old_price_int + y
            prices.append(re.sub(' +', ' ', price_int))
            discount.append("With Discount")
            old_price.append(old_price_int)
            percent.append(math.floor((int(old_price_int) - int(price_int)) / int(old_price_int) * 100))

    for i in soup.find_all("div", class_="product-grid-product-info__product-header"):
        name_str = i.find("h3")
        price_str = i.find("span", class_="money-amount__main").text

        price_int = ""

        for x in price_str:
            if x == ",":
                break
            if x.isdigit():
                price_int = price_int + x

        names.append(re.sub(' +', ' ', name_str.text.strip()))
        prices.append(price_int)
        brand.append("Zara")
        old_price.append("-")
        discount.append("No Discount")
        percent.append(0)

    for i in soup.find_all("div", class_="info"):
        name_str = i.find("h3", class_="title")
        price_str = i.find("div", class_="price").find("div").text
        discount_str = i.find("div", class_="basket-discount")
        names.append(name_str.text)
        brand.append("LC Waikiki")

        price_int = ""
        discount_int = ""

        if discount_str is None:
            for x in price_str:
                if x == ",":
                    break
                if x.isdigit():
                    price_int = price_int + x
            prices.append(price_int)
            discount.append("No Discount")
            old_price.append("-")
            percent.append(0)
        else:
            for x in price_str:
                if x == ",":
                    break
                if x.isdigit():
                    price_int = price_int + x
            for y in discount_str.text:
                if y == ",":
                    break
                if y.isdigit():
                    discount_int = discount_int + y
            prices.append(discount_int)
            old_price.append(price_int)
            discount.append("With Discount")
            percent.append(math.floor((int(price_int) - int(discount_int)) / int(price_int) * 100))

prices_int = []

for x in prices:
    prices_int.append(int(x))

print("Max Cost: " + str(max(prices_int)))
print("Min Cost: " + str(min(prices_int)))

data = {
    'name': names,
    'price': prices,
    'old price': old_price,
    'discount': discount,
    'brand': brand,
    'percent': percent
}

df = pd.DataFrame(data)
print(df)

df.to_csv('Output_csv.csv', encoding='utf-8')

with pd.ExcelWriter('Result_excel.xlsx') as writer:
    df.to_excel(writer, sheet_name='Sheet_1')
