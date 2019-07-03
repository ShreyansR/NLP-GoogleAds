'''
from requests import get
from bs4 import BeautifulSoup

<<<<<<< HEAD
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
=======

def com(url: str) -> str:
    """
    Takes a url and returns the text from that HTML page.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    html = (soup.prettify())
    print(html)
    lol = soup.findAll('div', attrs={'class':'ZINbbc'})
    thing = ''
    for item in lol:
        thing += item.text + "\n" + "\n"
    print("=======================")
    print(thing)






if __name__ == "__main__":
    keyword = input("Enter keyword: ")
    com("https://www.google.com/search?q="+keyword)

>>>>>>> 1c51ccacdf3426681d3da2c92d3d5a855617349e
