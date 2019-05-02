
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import shutil, os
import requests, urllib


def download_image(url, path):
    response = requests.get(url, stream=True)
    with open(path, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response




#shutterstock
NUMBER_OF_PAGES = 10
for page in range(1, NUMBER_OF_PAGES):
    site = 'https://www.shutterstock.com/search/transparent+background?page={}'.format(page)

    req = Request(site, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, 'html.parser')

    table = soup.find_all('img', attrs={'class': 'z_e_h'})

    for image in table:
        image_link = image.get('src')
        path = os.path.join('shutterstock', image_link[-13:])
        download_image(image_link, path)

