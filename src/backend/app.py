from operator import mul
from os.path import join
from flask import Flask, flash, request, redirect, url_for, session
from flask.wrappers import Response
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin
from Matrixterm import generateTermsFromFiles, generateQueryVector, updateTerms, generateTermsFromWebscrap
from vectorizer import sim
from webscrape import getFirstSentence, wordsCount
from os import listdir
from os.path import isfile, join

import html
import os
import json
import ast
import operator

from flask.templating import render_template

UPLOAD_DIRECTORY = "/static"
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'html'])

app = Flask(__name__)
app.config['UPLOAD_DIRECTORY'] = UPLOAD_DIRECTORY
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
CORS(app)
basedir = os.path.abspath(os.path.dirname(__file__))


@app.route('/api/search', methods=['GET'])
# FullMatrix[0] = uniqueTerms
def dir():
    query = request.args.get('query', default="", type=str)
    [uniqueTerms, fullMatrix, fileNames] = generateTermsFromFiles(basedir)
    queryVector = generateQueryVector(query)
    minQueryVector = queryVector.copy()  # Shallow copy dari query vector

    if (len(queryVector) == 0):
        response = dict()
        rank = dict()
        rank['title'] = "stopwords"
        response['ranks'] = []
        response['ranks'].append(rank)
        return response

    termsContainer = {
        x: queryVector[x] if x in queryVector else 0 for x in uniqueTerms}
    queryVector.update(termsContainer)
    fullMatrix = updateTerms(fullMatrix, queryVector)

    # buat baca list directory
    onlyfiles = [f for f in listdir(
        basedir + UPLOAD_DIRECTORY) if isfile(join(basedir + UPLOAD_DIRECTORY, f))]
    multFiles = []
    for f in onlyfiles:
        multFiles.append(os.path.splitext(f)[0])

    response = dict()
    response['ranks'] = []
    Di_terms = dict()
    for keys in minQueryVector:
        Di_terms[keys] = fullMatrix[0][keys]
    response['table'] = []
    response['table'].append(Di_terms)
    response['table'].append(minQueryVector)
    for i in range(1, len(fullMatrix)):
        rank = dict()
        rank['title'] = fileNames[i]
        rank['similarity'] = sim(queryVector, fullMatrix[i])
        rank['header'] = open(os.path.join(
            basedir + "/static", fileNames[i])).readline()
        wordscount = 0
        for keys in fullMatrix[i]:
            wordscount += fullMatrix[i][keys]
        rank['wordscount'] = wordscount
        response['ranks'].append(rank)
        Di_terms = dict()
        for keys in minQueryVector:
            Di_terms[keys] = fullMatrix[i][keys]
        response['table'].append(Di_terms)
    response['kolom'] = []
    response['kolom'].append(multFiles)
    response['ranks'].sort(key=operator.itemgetter('similarity'), reverse=True)
    return json.dumps(response)


@app.route('/api/webscrap', methods=['GET'])
def webdir():
    query = request.args.get('query', default="", type=str)
    [uniqueTerms, fullMatrix, webs] = generateTermsFromWebscrap()
    queryVector = generateQueryVector(query)
    if (len(queryVector) == 0):
        response = dict()
        response['ranks'] = [
            {"title": "no results, maybe all your search query are stopwords"}]
        return response
    minQueryVector = queryVector.copy()  # Shallow copy dari query vector

    termsContainer = {
        x: queryVector[x] if x in queryVector else 0 for x in uniqueTerms}
    queryVector.update(termsContainer)
    fullMatrix = updateTerms(fullMatrix, queryVector)

    response = dict()
    response['ranks'] = []
    response['kolom'] = [['https://www.worldoftales.com/fairy_tales/Hans_Christian_Andersen/Andersen_fairy_tale_47.html#gsc.tab=0',
                          'https://www.worldoftales.com/fairy_tales/Brothers_Grimm/Grimm_fairy_stories/Cinderella.html#gsc.tab=0', 'https://www.worldoftales.com/European_folktales/English_folktale_116.html#gsc.tab=0']]
    Di_terms = dict()
    for keys in minQueryVector:
        Di_terms[keys] = fullMatrix[0][keys]
    response['table'] = []
    response['table'].append(Di_terms)
    response['table'].append(minQueryVector)
    for i in range(1, len(fullMatrix)):
        rank = dict()
        rank['title'] = webs[i-1]
        rank['similarity'] = sim(queryVector, fullMatrix[i])
        rank['header'] = getFirstSentence(rank['title'])
        rank['wordscount'] = wordsCount(rank['title'])
        response['ranks'].append(rank)
        Di_terms = dict()
        for keys in minQueryVector:
            Di_terms[keys] = fullMatrix[i][keys]
        response['table'].append(Di_terms)

    response['ranks'].sort(key=operator.itemgetter('similarity'), reverse=True)
    return json.dumps(response)


@app.route('/api/basedir', methods=['GET'])
def what_ismy_basedir():
    return basedir


@app.route('/api/cerita/', methods=['GET'])
def fetchCerita():
    cerita = request.args.get('cerita', default="", type=str)
    data = open(os.path.join(basedir, 'static/'+cerita)).read()
    return data


@app.route("/api/upload", methods=['POST'])
def upload_files():
    target = os.path.join(basedir + UPLOAD_DIRECTORY)
    if not os.path.isdir(target):
        os.mkdir(target)
    file = request.files['file']
    filename = secure_filename(file.filename)
    destination = "/".join([target, filename])
    file.save(destination)
    session['uploadFilePath'] = destination
    response = "apa aja dah"
    return response


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
