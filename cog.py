import requests
import json
import beautifulscraper
from bs4 import BeautifulSoup
import re



def com() -> str:
    """
    Takes a url and returns the text from that HTML page.
    """

    vision_base_url = "https://www.google.com/search?q=phone+plans&oq=phone+plans&aqs=chrome.0.69i59j0l5.2207j0j7&sourceid=chrome&ie=UTF-8"

    response = requests.get(vision_base_url)

    # make sure response is 200 OK
    print(response)
    soup = BeautifulSoup(response.text)

    # cuts the scripts out
    for script in soup(["script", "style"]):
        script.decompose()

    text = soup.get_text("|", strip=True)

    # cleans the data
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)

    return text[273:]


if __name__ == "__main__":
    text = com()
    file = open("StrippedText.txt", "w")
    file.write(text)
    file.close()
    print(text)
