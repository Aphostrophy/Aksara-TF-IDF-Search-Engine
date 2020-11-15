from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import collections

        
def webscrape(url):
    my_url=url
    uClient = uReq(my_url)
    page_soup = soup(uClient.read(), "html.parser")
    uClient.close()

    s = page_soup.find('div', class_='GM')

    for child in s.find_all("div"):
        child.decompose()

    x =s.get_text()
    text_tokens = word_tokenize(x)
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

    s = page_soup.find('div', class_='GM')

    for child in s.find_all("div"):
        child.decompose()

    x =s.get_text()

    s=""
    i=0
    while x[i] != '.':
        s+=str(x[i])
        i=i+1
    s+='.'   
    return s


def wordsCount(url):
    my_url=url
    uClient = uReq(my_url)
    page_soup = soup(uClient.read(), "html.parser")
    uClient.close()

    s = page_soup.find('div', class_='GM')

    for child in s.find_all("div"):
        child.decompose()

    x =s.get_text()
    y = x.split()

    count =0
    for i in y:
        count = count+1

    return count

    

