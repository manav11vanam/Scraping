import requests
from bs4 import BeautifulSoup

url = 'https://geeksforgeeks.org/'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'lxml')
print(soup)
print('*'*100)
print(soup.prettify())
print('*'*100)
# soup.get_all('div')
# soup['div']
# li = [el for el in soup if el['class']=='cookie-consent']
# print(li)
# print(a_tag)
# print('*'*100)
print(len(list(a_tag.children)))

# for i in a_tag.children:
#     print(i)
#     print('*'*100)
