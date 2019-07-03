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

    # make sure response is 200 OK
    try:
        assert response.ok is True

        soup = BeautifulSoup(response.text, "html.parser")

        # cuts the scripts out
        for script in soup(["script", "style"]):
            script.decompose()

        text = soup.get_text("|", strip=True)

        # cleans the data
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = '\n'.join(chunk for chunk in chunks if chunk)

        return text
    except:
        print("error: response times out")



if __name__ == "__main__":
    keyword = input("Enter keyword: ")
    other = com("https://www.google.com/search?q="+keyword)
    file = open("StrippedText.txt", "w")
    file.write(other)
    file.close()
    print(other)
