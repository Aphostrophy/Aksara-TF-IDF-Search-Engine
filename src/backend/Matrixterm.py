import os
from filtering import Cleaningkata, Cleaningquery, convert, Countwords
from webscrape import webscrape


def generateTermsFromFiles(basedir):
    basedir = basedir + "/static"
    multFiles = []
    uniqueTerms = dict()  # Declare Empty Dict untuk nyimpen semua unique terms
    fullMatrix = []  # array of dict
    fileNames = ["skip this"]
    for filenames in os.listdir(basedir):
        if filenames.endswith(".html"):
            fileNames.append(filenames)
            joinpath = os.path.join(basedir, filenames)
            file = open(joinpath).read()
            docs = convert(Cleaningkata(file))
            docs = docs.split()
            docs = Countwords(docs)
            termDocs = docs.copy()
            termDocs = {x: 0 for x in termDocs}  # Dictionary comprehension
            uniqueTerms.update(termDocs)
            multFiles.append(docs)
        else:
            continue
    return generateMatrixFromTerms(fullMatrix, uniqueTerms, multFiles, fileNames)


def generateMatrixFromTerms(fullMatrix, uniqueTerms, multFiles, fileNames):
    elem = dict()
    for keys in uniqueTerms:
        elem[keys] = 0
    fullMatrix.append(elem)
    for docs in multFiles:
        elem = dict()
        for keys in uniqueTerms:
            if keys in docs:
                elem[keys] = docs[keys]
            else:  # keys not in docs
                elem[keys] = 0
        fullMatrix.append(elem)

    return [uniqueTerms, fullMatrix, fileNames]


def generateTermsFromWebscrap():
    fullMatrix = []
    semiFullMatrix = []
    uniqueTerms = dict()
    webs = ['https://www.worldoftales.com/fairy_tales/Hans_Christian_Andersen/Andersen_fairy_tale_47.html#gsc.tab=0',
            'https://www.worldoftales.com/fairy_tales/Brothers_Grimm/THE%20GOOSE-GIRL.html#gsc.tab=0', 'https://www.worldoftales.com/European_folktales/English_folktale_116.html#gsc.tab=0']
    for web in webs:
        docs = webscrape(web)
        termDocs = docs.copy()
        termDocs = {x: 0 for x in termDocs}
        uniqueTerms.update(termDocs)
        semiFullMatrix.append(docs)
    return generateMatrixFromWebTerms(uniqueTerms, fullMatrix, semiFullMatrix, webs)


def generateMatrixFromWebTerms(uniqueTerms, fullMatrix, semiFullMatrix, webs):
    elem = dict()
    for keys in uniqueTerms:
        elem[keys] = 0
    fullMatrix.append(elem)
    for docs in semiFullMatrix:
        elem = dict()
        for keys in uniqueTerms:
            if keys in docs:
                elem[keys] = docs[keys]
            else:
                elem[keys] = 0
        fullMatrix.append(elem)
    return [uniqueTerms, fullMatrix, webs]


def generateQueryVector(query):
    docs = convert(Cleaningquery(query))
    docs = docs.split()
    return Countwords(docs)


def updateTerms(fullMatrix, queryVector):
    newFullMatrix = []
    for docsDict in fullMatrix:
        tempDocsDict = docsDict.copy()
        docsDict = {x: 0 for x in queryVector}
        docsDict.update(tempDocsDict)
        newFullMatrix.append(docsDict)
    return newFullMatrix  # terms newFullMatrix sudah lengkap bersama query

# for docs in multFiles:
#     print("File: ")
#     print(docs)

# print(uniqueTerms)
# print(fullMatrix)

# for i in range(len(fullMatrix)):
#     print(len(fullMatrix[0]))
