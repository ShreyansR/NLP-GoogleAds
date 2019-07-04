import requests
from bs4 import BeautifulSoup
import re
import io
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from wordcloud import WordCloud
import matplotlib.pyplot as plt

stopwords = set(stopwords.words('english'))

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

    #print(thing)
    return thing


if __name__ == "__main__":
    keyword = input("Enter keyword: ")
    other = com("https://www.google.com/search?q="+keyword)
    other = other.replace("|", "")
    file = open("StrippedText.txt", "w")
    file.write(other)
    tokens = word_tokenize(other)
    freq = nltk.FreqDist(tokens)
    wordcloud = WordCloud().generate_from_frequencies(freq)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()
    file.close()