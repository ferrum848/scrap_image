
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import shutil, os
import requests, urllib


def download_image(url, path):
    response = requests.get(url, stream=True)
    with open(path, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response


#pngmart
list_of_categores = []

site = 'http://www.pngmart.com'
req = Request(site, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')
table = soup.find_all('dl', attrs={'class': 'gallery-item'})

for i in table:
    if i.find('a'):
        category = i.find('a').get('href')
        list_of_categores.append(category.split('/')[3])

for category in list_of_categores:
    os.makedirs(os.path.join(os.getcwd(), 'pngmart', category))
    category_tags = []
    site = 'http://www.pngmart.com/image/category/animals'
    req = Request(site, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, 'html.parser')

    table = soup.find('div', attrs={'class': 'category_tags'}).find_all('a')

    for i in table:
        category_tags.append(i.get('href'))
        subcategory = i.get('href')
        subdir = subcategory.split('/')[5]
        os.makedirs(os.path.join(os.getcwd(), 'pngmart', category, subdir))
        file_name = 1

        NUMBER_OF_PAGES = 5
        for page in range(1, NUMBER_OF_PAGES):
            site = subcategory + '/page/{}'.format(page)
            req = Request(site, headers={'User-Agent': 'Mozilla/5.0'})
            try:
                webpage = urlopen(req).read()
            except urllib.error.HTTPError:
                break

            soup = BeautifulSoup(webpage, 'html.parser')
            table = soup.find_all('div', attrs={'class': 'featuredimage'})
            for image in table:
                print(image.find('img').get('src'))
                image_link = image.find('img').get('src')
                path = os.path.join('pngmart', category, subdir, str(file_name) + '.png')
                download_image(image_link, path)
                file_name += 1



