import nltk
from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords


porter = PorterStemmer()

stopWords = set(stopwords.words('english'))


def stemkata(kata):
    token_words = word_tokenize(kata)
    token_words
    stem_kata = []
    for word in token_words:
        if not word in stopWords:
            stem_kata.append(porter.stem(word))
            stem_kata.append(" ")
    return "".join(stem_kata)


file = open("./testing/threeFeathers.html", "r")
print(file)
file = BeautifulSoup(file, 'html.parser')
print(file)

myLineList = []
for line in file:
    lineFilter = stemkata(line)
    myLineList.append(lineFilter)

for line in myLineList:
    print(line)
# print("Stemmed kata")

# x = stemkata(LineList[0])

# print(x)
