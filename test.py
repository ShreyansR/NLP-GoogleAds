import requests
from bs4 import BeautifulSoup


def com(url: str) -> str:
    """
    Takes a url and returns the text from that HTML page.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    html = (soup.prettify())
    print(html)
    lol = soup.findAll('div', attrs={'class':'MUxGbd yDYNvb aLF0Z'})
    thing = ''
    for item in lol:
        thing += item.text + "\n" + "\n"
    print("=======================")
    return thing


if __name__ == "__main__":
    keyword = input("Enter keyword: ")
    other = com("https://www.google.com/search?q="+keyword)
    file = open("StrippedText.txt", "w")
    file.write(other)
    file.close()
