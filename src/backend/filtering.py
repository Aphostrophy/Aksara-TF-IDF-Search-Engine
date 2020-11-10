from os import write
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from bs4 import BeautifulSoup
import re
import string
from CountWords import Countwords

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


def Cleaningkata(file):
    cleantext = BeautifulSoup(file, "html.parser").text
    x = stemkata(cleantext)
    clean_document = []
    for document in x:
        document = re.sub(r'[^\x00-\x7F]+', ' ', document)
        document = re.sub(r'@\w+', '', document)
        document = document.lower()
        document = re.sub(r'[%s]' % re.escape(
            string.punctuation), ' ', document)
        document = re.sub(r'\s{2,}', ' ', document)
        clean_document.append(document)
    return clean_document


def convert(str):
    new = ""
    for x in str:
        new += x
    return new


docs = convert(Cleaningkata(file))
docs = docs.split()

print(Countwords(docs))
