import requests
import json
import beautifulscraper
from bs4 import BeautifulSoup
import re


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

