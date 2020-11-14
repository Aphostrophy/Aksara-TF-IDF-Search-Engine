from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import collections

def listToString(s):  
    str1 = " "   
    return (str1.join(s)) 
        
def webscrape(url):
    my_url=url
    uClient = uReq(my_url)
    page_soup = soup(uClient.read(), "html.parser")
    uClient.close()

    whitelist = [
    'p',
    'pre'
    ]

    text_elements = [t for t in page_soup.findAll(text=True) if (t.parent.name in whitelist)]
    string = listToString(text_elements)
    text_tokens = word_tokenize(string)
    string_no_sw = [word.lower() for word in text_tokens if ((not word in stopwords.words('english')) and  word.isalpha())]

    myDict=[dict() for i in range(len(string_no_sw)) ]
    for j in range (len(string_no_sw)):
        myDict[j]=dict({string_no_sw[j] : 1})

    counter = collections.Counter() 
    for d in myDict:  
        counter.update(d) 
        
    result = dict(counter)
    return result

def getFirstSentence(url):
    my_url=url
    uClient = uReq(my_url)
    page_soup = soup(uClient.read(), "html.parser")
    uClient.close()

    whitelist = [
    'p',
    'pre'
    ]

    text_elements = [t for t in page_soup.findAll(text=True) if (t.parent.name in whitelist)]
    string = listToString(text_elements)

    s=""
    i=0
    while string[i] != '.':
        s+=str(string[i])
        i=i+1
    s+='.'   
    return s


