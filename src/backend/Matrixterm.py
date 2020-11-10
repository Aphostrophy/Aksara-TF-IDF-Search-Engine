import os
from filtering import Cleaningkata, Cleaningquery, convert, Countwords

def generateTermsFromFiles(basedir):
    basedir = basedir + "/static"
    multFiles = []
    uniqueTerms = dict() #Declare Empty Dict untuk nyimpen semua unique terms
    fullMatrix = [] #array of dict
    for filenames in os.listdir(basedir):
        if filenames.endswith(".txt"):
            joinpath = os.path.join(basedir, filenames)
            file = open(joinpath).read()
            docs = convert(Cleaningkata(file))
            docs = docs.split()
            docs = Countwords(docs)
            termDocs = docs.copy()
            termDocs = {x:0 for x in termDocs} #Dictionary comprehension
            uniqueTerms.update(termDocs)
            multFiles.append(docs)
        else:
            continue
    return generateMatrixFromTerms(fullMatrix,uniqueTerms,multFiles)

def generateMatrixFromTerms(fullMatrix,uniqueTerms,multFiles):
    elem = dict()
    for keys in uniqueTerms:
        elem[keys] = 0
    fullMatrix.append(elem)
    for docs in multFiles:
        elem = dict()
        for keys in uniqueTerms:
            if keys in docs:
                elem[keys]=docs[keys]
            else: #keys not in docs
                elem[keys]=0
        fullMatrix.append(elem)

    return [uniqueTerms, fullMatrix]

def generateQueryVector(query):
    docs = convert(Cleaningquery(query))
    docs = docs.split()
    return Countwords(docs)

def updateTerms(fullMatrix,queryVector):
    newFullMatrix= []
    for docsDict in fullMatrix:
        tempDocsDict = docsDict.copy()
        docsDict = {x:0 for x in queryVector}
        docsDict.update(tempDocsDict)
        newFullMatrix.append(docsDict)
        print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
        print(docsDict)
    return newFullMatrix

# for docs in multFiles:
#     print("File: ")
#     print(docs)

# print(uniqueTerms)
# print(fullMatrix)

# for i in range(len(fullMatrix)):
#     print(len(fullMatrix[0]))