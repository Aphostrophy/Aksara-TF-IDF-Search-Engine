import nltk
from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from bs4 import BeautifulSoup


porter = PorterStemmer()

stopWords = set(stopwords.words('english'))


def stemkata(kata):
    token_words = word_tokenize(kata)
    stem_kata = []
    for word in token_words:
        if not word in stopWords:
            stem_kata.append(porter.stem(word))
            stem_kata.append(" ")
    return "".join(stem_kata)

file = open("./static/threePrincess.html").read()

cleantext = BeautifulSoup(file, "html.parser").text

print("Stemmed kata")
x = stemkata(cleantext)
print(x)
