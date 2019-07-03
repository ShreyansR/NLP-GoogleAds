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
    print(text)

    # analysis = response.json()
    # print(json.dumps(analysis))