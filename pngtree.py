
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import shutil, os
import requests, urllib


def download_image(url, path):
    response = requests.get(url, stream=True)
    with open(path, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response




#pngtree
list_of_usage = []

site = 'https://pngtree.com/free-png'
req = Request(site, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')

list_of_usage = []

table = soup.find_all('div')
for i in table:
    temp = i.find('a', attrs={'class': 'sort-btn'})
    if temp:
        if temp.text != 'All':
            list_of_usage.append(temp.get('href'))

if len(list_of_usage) == 0:
    list_of_usage = ['/free-animals-png', '/free-star-png', '/free-music-png', '/free-christmas-png', '/free-hearts-png', '/free-arrows-png', '/free-flower-png', '/free-tree-png', '/free-logo-png', '/free-cars-png', '/free-people-png', '/free-cloud-png', '/free-light-png', '/free-ribbons-png', '/free-line-png', '/free-circle-png', '/free-birthday-png', '/free-water-png', '/free-bird-png', '/free-sun-png', '/free-grass-png', '/free-fire-png', '/free-halloween-png', '/free-smoke-png', '/free-crown-png', '/free-explosion-png', '/free-autumn-png']
else:
    list_of_usage = list_of_usage[4:]

NUMBER_OF_PAGES = 3
for category in list_of_usage:
    file_name = 1
    subdir = category.split('-')[1]
    os.makedirs(os.path.join(os.getcwd(), 'pngtree', subdir))
    for page in range(1, NUMBER_OF_PAGES):
        site = 'https://pngtree.com' + category +  '/' + str(page)
        print(site)

        req = Request(site, headers={'User-Agent': 'Mozilla/5.0'})
        webpage = urlopen(req).read()
        soup = BeautifulSoup(webpage, 'html.parser')

        table = soup.find_all('div', attrs={'class': 'mb-picbox'})
        for i in table:
            image_link = i.find('img').get('data-original')
            path = os.path.join('pngtree', subdir, str(file_name) + '.jpg')
            download_image(image_link, path)
            file_name += 1

