import requests
from bs4 import BeautifulSoup
import csv

urlo = 'http://quotes.toscrape.com'
url = urlo[:]
counter = 0
with open('quotes.csv', 'w', newline='', encoding='utf-8') as csv_write_file:
    headings = ['Quote', 'Author']
    csv_writer = csv.DictWriter(csv_write_file, fieldnames=headings, delimiter='-')
    csv_writer.writeheader()
    while url is not None:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.content, 'lxml')
        divs = soup('div', class_='quote')

        for div in divs:
            quote = div('span', class_="text")[0].text[1:-1]
            author = div.small.text
            print(quote)
            print("\n-",author)
            print('\n' + '*'*100)
        # try:
            csv_writer.writerow({"Quote": quote, "Author": author})
        # except:
        #     print("#"*100+"\nCouldn't write so skipped")
        li = soup('li', class_='next')
        if li==[]:
            url = None
        else:
            url = urlo + li[0].a.get('href')

        print(url)
