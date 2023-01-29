import requests
from bs4 import BeautifulSoup
import os

search_term = "example"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;Win64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
           'Host': 'www.ebay-kleinanzeigen.de',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
           'Accept-Language': 'en-US,en;q=0.9',
           'Accept-Encoding': 'gzip, deflate, br',
           'Connection': 'keep-alive'}

def download_images(url, name):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    images = soup.find_all('img')
    for i, image in enumerate(images[:4]):
        img_url = image['src']
        response = requests.get(img_url, headers=headers)
        open(f"{name}_{i}.jpg", "wb").write(response.content)

response = requests.get(f"https://www.ebay-kleinanzeigen.de/s-autos/smart/anzeige:angebote/smart/k0c216+autos.marke_s:smart+autos.schaden_s:nein", headers=headers)#
print(response.text)
soup = BeautifulSoup(response.content, 'html.parser')
ads = soup.find_all('a', {'class': 'ellipsis'})
for ad in ads:
    title = ad.get_text()
    link = 'https:/' + ad['href']
    download_images(link, title)
