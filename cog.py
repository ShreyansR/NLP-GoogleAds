import requests
import json
import beautifulscraper
from bs4 import BeautifulSoup
import re

def com() -> None:

    vision_base_url = "https://www.google.com/search?q=phone+plans&oq=phone+plans&aqs=chrome.0.69i59j0l5.2207j0j7&sourceid=chrome&ie=UTF-8"

    response = requests.get(vision_base_url)
    print(response)
    soup = BeautifulSoup(response.text)

    for script in soup(["script", "style"]):
        script.decompose()

    text = soup.get_text("|", strip=True)

    lines = (line.strip() for line in text.splitlines())

    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)

    file = open("StrippedText.txt", "w")
    file.write(text)
    file.close()
    print(text)


if  __name__=="__main__":
    com()