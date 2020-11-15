from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import collections


#Fungsi ini berfungsi untuk menghasilkan array of dictionary dari konten teks suatu web yang sudah distemming 
def webscrape(url):
    my_url=url
    uClient = uReq(my_url) #send request
    page_soup = soup(uClient.read(), "html.parser") #parse html yang didapat dengan lib beautifulsoup
    uClient.close()

    s = page_soup.find('div', class_='GM') #cari elemen dengan parent tag div dan class 'GM'

    for child in s.find_all("div"): #hilangkan seluruh anak tag div dari div class 'GM'
        child.decompose()

    x =s.get_text() #mendapatkan text dari seleksi web yang sudah dilakukan
    text_tokens = word_tokenize(x) #tokenisasi text yang didapat
    string_no_sw = [word.lower() for word in text_tokens if ((not word in stopwords.words('english')) and  word.isalpha())] #hilangkan stopword dan tanda baca

    myDict=[dict() for i in range(len(string_no_sw)) ] #seluruh terms yang ada dijadikan dictionary dengan key = term dan value = 1
    for j in range (len(string_no_sw)):
        myDict[j]=dict({string_no_sw[j] : 1})

    counter = collections.Counter() #satukan seluruh dictionary dengan key yang sama, update value
    for d in myDict:  
        counter.update(d) 
        
    result = dict(counter)
    return result #return array of dictionary {term : jumlah term}

#Fungsi ini berfungsi untuk mendapatkan kalimat pertama dari konten teks suatu web
def getFirstSentence(url):
    my_url=url
    uClient = uReq(my_url) #send request
    page_soup = soup(uClient.read(), "html.parser") #parse html yang didapat dengan lib beautifulsoup
    uClient.close()

    s = page_soup.find('div', class_='GM') #cari elemen dengan parent tag div dan class 'GM'

    for child in s.find_all("div"): #hilangkan seluruh anak tag div dari div class 'GM'
        child.decompose()

    x =s.get_text() #mendapatkan text dari seleksi web yang sudah dilakukan

    s="" #inisiasi string kosong
    i=0
    while x[i] != '.': #iterasi perhuruf di x, apabila current character bukan titik maka char akan diappend ke string s
        s+=str(x[i])
        i=i+1
    s+='.'   #tambahkan titik di akhir
    return s

#Fungsi ini berfungsi untuk menghitung jumlah kata tanpa stemming pada konten teks suatu web
def wordsCount(url):
    my_url=url
    uClient = uReq(my_url) #send request
    page_soup = soup(uClient.read(), "html.parser") #parse html yang didapat dengan lib beautifulsoup
    uClient.close()

    s = page_soup.find('div', class_='GM') #cari elemen dengan parent tag div dan class 'GM'

    for child in s.find_all("div"): #hilangkan seluruh anak tag div dari div class 'GM'
        child.decompose()

    x =s.get_text() #mendapatkan text dari seleksi web yang sudah dilakukan
    y = x.split() #split text yang didapat menjadi array of kata (string)

    count =0
    for i in y:
        count = count+1 #hitung jumlah elemen pada array of kata

    return count

    

