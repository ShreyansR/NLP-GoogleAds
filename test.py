import requests
from bs4 import BeautifulSoup
import re

def com(url: str) -> str:
    """
    Takes a url and returns all the add text from that page
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    lol = soup.findAll('div', attrs={'class':'ZINbbc'})
    thing = ''
    for item in lol:
        # clean = item.text + "\n" + "\n"
        #
        # if re.findall("(.+)Adwww(.+)", clean):
        #     thing += clean

        if item.findAll("div", attrs={'class': "MUxGbd"}):
            thing += item.text + "\n" + "\n"
    print(thing)
    return thing


if __name__ == "__main__":
    keyword = input("Enter keyword: ")
    other = com("https://www.google.com/search?q="+keyword)
    file = open("StrippedText.txt", "w")
    file.write(other)
    file.close()
