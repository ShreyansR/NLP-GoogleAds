import requests
import json
import beautifulscraper
from bs4 import BeautifulSoup
import re
import nltk
import cog
import re

def nlp(url: str) -> str:
    """
    Takes a url and returns the text from that HTML page.
    """
    text = cog.com(url)
    tokens = [t for t in text.split()]
    print(tokens)

    # plots the frequency of key words
    from nltk.corpus import stopwords
    sr = stopwords.words('english')
    clean_tokens = tokens[:]
    for token in tokens:
        if token in stopwords.words('english'):
            clean_tokens.remove(token)
    freq = nltk.FreqDist(clean_tokens)
    for key, val in freq.items():
        print(str(key) + ':' + str(val))
    freq.plot(20, cumulative=False)

def phone():
    """

    :return:
    """
    text = cog.com("https://www.google.com/search?q=phone+plans&oq=phone+plans&aqs=chrome.0.69i59j0l5.2207j0j7&sourceid=chrome&ie=UTF-8")
    print(type(text))


def other():
    """
    downloads nltk packages
    :return:
    """

    import nltk
    import ssl

    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context

    nltk.download()


if __name__ == "__main__":
    nlp("https://www.google.com/search?q=phone+plans&oq=phone+plans&aqs=chrome.0.69i59j0l5.2207j0j7&sourceid=chrome&ie=UTF-8")
