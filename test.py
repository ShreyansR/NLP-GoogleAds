'''
from requests import get
from bs4 import BeautifulSoup

keyword = input("Enter keyword: ")
url = "https://www.google.com/search?q=" + keyword

response = get(url)
soup = BeautifulSoup(response.text, 'html.parser')
html = soup.prettify()
print(html)
#container = soup.find_all('div', classmethod = 'g')
#print(type(container))
#print(len(container))
'''