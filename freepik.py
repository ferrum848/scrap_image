
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import shutil, os
import requests, urllib


def download_image(url, path):
    response = requests.get(url, stream=True)
    with open(path, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response


START_PAGE = 1
file_name = 1
site_main = 'https://www.freepik.com'
next_link = '/search?page={}&query=transparent&sort=popular'.format(START_PAGE)
while True:
    site = site_main + next_link
    req = Request(site, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, 'html.parser')
    table = soup.find_all('img', attrs={'class': 'lzy'})
    for link in table:
        image_link = link.get('data-src').split('?')[0]
        path = os.path.join('freepik', str(file_name) + '.jpg')
        download_image(image_link, path)
        file_name += 1

    table = soup.find('div', attrs={'class': 'pagination__button clearfix'})
    try:
        next_link = table.find('a', attrs={'class': 'pagination__next'}).get('href')
    except AttributeError:
        break




