from bs4 import BeautifulSoup
import requests

# with open('simple.html') as html_file:
#     soup = BeautifulSoup(html_file, 'lxml')

# print(soup.prettify())
# print(soup.title)
# print(soup.title.text)
# print(soup.find('div', class_='article'))
# print(soup.find_all('div', class_='article'))
# print(soup.find_all('script', src="js/vendor/modernizr-3.5.0.min.js"))
# print(soup('div', class_ = 'article'))
# print('\n\n')

# articles = soup('div', class_ = 'article')
# for article in articles:
#     headline = article.h2.a.text
#     print(headline)
#     summary = article.p.text
#     print(summary)
#     print("-"*50)


'''_____________________________________________________________________________________________________________________________'''

search_url = 'https://coreyms.com/'
response = requests.get(search_url, timeout = 5)
if not response.status_code == 200 :
    print("Failed")
    quit()
html = response.text
soup = BeautifulSoup(html, 'lxml')
# tags = soup('article')
# for tag in tags:
#     print(tag.prettify())
#     print('-'*75)
#
# tag = soup.find('article')
# print(tag.prettify())
# print('-'*75)
# embeddedlink = tag.iframe.get('src',None)
# vid_id = embeddedlink.split('/')[4].split('?')[0]
# ytlink = f'https://youtube.com/watch?v={vid_id}'
# print(ytlink)


# tags = soup('article')
# for tag in tags:
#     ifr = tag.iframe
#     if ifr is None: continue
#     print(tag.h2.a.text)
#     print(tag.div.p.text)
#     embeddedlink = ifr.get('src',None)
#     vid_id = embeddedlink.split('/')[4].split('?')[0]
#     ytlink = f'https://youtube.com/watch?v={vid_id}'
#     print(ytlink)
#     print('-'*75)


tags = soup('article')
for tag in tags:
    print(tag.h2.a.text)
    print(tag.div.p.text)
    try:
        embeddedlink = tag.iframe.get('src',None)
        vid_id = embeddedlink.split('/')[4].split('?')[0]
        ytlink = f'https://youtube.com/watch?v={vid_id}'
        print(ytlink)
    except:
        print('No video link available')
    print('-'*75)
