import requests
from bs4 import BeautifulSoup
import pdb
url = 'http://books.toscrape.com/'
orig_url = 'http://books.toscrape.com/catalogue/'

''' Prdouct name and cost '''
star_rating = {'One' : 1, 'Two' : 2,'Three' : 3,'Four' : 4,'Five' : 5}
page_count = 0
while url is not None:
    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.content, 'lxml')
    articles = soup('article', class_='product_pod')
    for article in articles:
        name = article.h3.a.get('title')
        div_tag = article('div', class_='product_price')[0]
        price = div_tag.p.text
        rating_p_tag = article.find('p')
        rating = star_rating[rating_p_tag.get('class')[1]]
        print(name, price, 'Rating:', rating)
    li_tag = soup.find('li', class_='next')
    ht = li_tag.a.get('href')
    if ht.startswith('catalog'):
        url += ht
    else:
        url = orig_url + str(ht)
    print(f'Page {page_count+1} completed')
    page_count += 1
