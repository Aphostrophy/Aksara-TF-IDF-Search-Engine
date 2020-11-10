import os
from filtering import Cleaningkata, convert
from CountWords import Countwords

basedir = os.path.abspath(os.path.dirname(__file__)) + "/static"
multFiles = []
uniqueTerms = dict() #Declare Empty Dict untuk nyimpen semua unique terms
fullMatrix = [] #array of dict

def generateTermsFromFiles(basedir,uniqueTerms,multFiles):
    for filenames in os.listdir(basedir):
        if filenames.endswith(".html"):
            joinpath = os.path.join(basedir, filenames)
            file = open(joinpath).read()
            docs = convert(Cleaningkata(file))
            docs = docs.split()
            docs = Countwords(docs)
            uniqueTerms.update(docs)
            multFiles.append(docs)
        else:
            continue

def generateMatrixFromTerms(fullMatrix,uniqueTerms,multFiles):
    elem = dict()
    for keys in uniqueTerms:
        elem[keys] = 1
    fullMatrix.append(elem)
    for docs in multFiles:
        elem = dict()
        for keys in uniqueTerms:
            if keys in docs:
                elem[keys]=docs[keys]
            else: #keys not in docs
                elem[keys]=0
        fullMatrix.append(elem)
    

generateTermsFromFiles(basedir,uniqueTerms,multFiles)

generateMatrixFromTerms(fullMatrix,uniqueTerms,multFiles)

# for docs in multFiles:
#     print("File: ")
#     print(docs)

# print(uniqueTerms)
print(fullMatrix)

for i in range(len(fullMatrix)):
    print(len(fullMatrix[0]))