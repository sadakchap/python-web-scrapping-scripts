from bs4 import BeautifulSoup
import requests
import csv

csv_file = open('cms_data.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Product Name', 'image_link', 'price', 'product_link'])

# site to be scraped

source = requests.get(
    'https://www.amazon.com/s/browse?_encoding=UTF8&node=16225007011&ref_=nav_shopall-export_nav_mw_sbd_intl_computers').text

# scraping starts

soup = BeautifulSoup(source, 'lxml')

for product in soup.find_all('div', class_='s-item-container'):
    try:
        pro_link = product.find(
            'a', class_=['a-link-normal', 'a-text-normal']).get('href')
        pro_name = product.find(
            'h2', class_=['a-size-base', 's-inline', 's-access-title']).text
        image_link = product.find(
            'img', class_=['s-access-image', 'cfMarker'])['src']
        price = product.find('span', class_='a-offscreen').text

        print(pro_link, image_link, pro_name, price, sep='\n')
        print('*' * 90)
        csv_writer.writerow([pro_name, image_link, price, pro_link])
    except:
        pass


csv_file.close()
