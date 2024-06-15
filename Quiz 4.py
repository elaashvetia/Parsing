import requests
from bs4 import BeautifulSoup
import time
import csv
from random import randint

file = open('whiskey.csv', 'w', encoding='utf-8_sig', newline='\n')
write_obj = csv.writer(file)
write_obj.writerow(['დასახელება', 'მოცულობა', 'ფასი', 'სურათი'])

page = 1
while page <= 5:
    url = f'https://alcorium-store.ge/%E1%83%95%E1%83%98%E1%83%A1%E1%83%99%E1%83%98-ka/page-{page}/?sort_by=price&sort_order=asc'
    response = requests.get(url)
    # print(response.status_code)
    # print(response.headers)
    content = response.text

    soup = BeautifulSoup(content, 'html.parser')
    whiskey_section = soup.find('div', id='categories_view_pagination_contents')
    all_whiskey = whiskey_section.find_all('div', class_='ty-product-list clearfix')
    for each in all_whiskey:
        right = each.find('div', class_='ut2-pl__content')
        title = right.bdi.a.text[:-8]
        volume = right.bdi.a.text[-5:].strip()
        price = right.find('span', class_='ty-price-num').text
        img = each.img.attrs.get('data-src')
        write_obj.writerow([title, volume, price, img])
    page += 1
    time.sleep(randint(15, 20))