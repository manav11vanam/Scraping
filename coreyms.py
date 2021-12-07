import requests
from bs4 import BeautifulSoup
import re

url = 'https://coreyms.com/'
with open('coreyms.txt', 'w', newline='\n') as fh:
    while url is not None:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.content, 'lxml')
        articles = soup('article')
        for article in articles:
            print(article.h2.a.text)
            fh.write(article.h2.a.text + '\n')
            print("Date published:",article.time.text)
            fh.write("Date published: "+ article.time.text)
            div_class = article("div", class_='entry-content')[0]
            print(div_class.p.text)
            fh.write(div_class.p.text + '\n')
            try:
                vid_link = article.iframe.get('src', None)
                vid_id = re.findall('/([a-zA-Z0-9_\-!@#$%^&*]+?)\?', vid_link)[0]
                link = "https://youtube.com/watch?v=" + str(vid_id)
            except:
                link = None
            print("Link:", link)
            fh.write("Link: "+ str(link) + '\n')
            print('*'*100)
            fh.write('*'*100 + '\n')
        try:
            url = soup('li', class_='pagination-next')[0].a.get('href', None)
        except:
            print("We're done man!")

#https://youtube.com/watch?v=video_id
# <li class="pagination-next"><a href="https://coreyms.com/page/2">Next Page »</a></li>
