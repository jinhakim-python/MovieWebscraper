from bs4 import BeautifulSoup
import requests

x = input(str())
searchs = [x]

for search in searchs:
    url = f"https://movies123.email/search/{search}/"
    data = requests.get(url)

    soup = BeautifulSoup(data.text, 'html.parser')

    imgs = soup.findAll('img')

    for img in imgs:
        print(img)
        with open('index.html', 'a+') as file:
            if img['data-original'] != 'https://movies123.email/promo/noposter.png':
                file.write(f"<img src={img['data-original']}>\n")