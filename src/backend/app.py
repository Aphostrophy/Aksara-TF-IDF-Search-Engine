from flask import Flask, flash, request, redirect, url_for, session
from flask.wrappers import Response
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin
# from Matrixterm import generateTermsFromFiles, generateQueryVector, updateTerms
from vectorizer import sim
import os
import json
import ast

from flask.templating import render_template

UPLOAD_DIRECTORY = "/static"
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'html'])

app = Flask(__name__)
app.config['UPLOAD_DIRECTORY'] = UPLOAD_DIRECTORY
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
CORS(app)
basedir = os.path.abspath(os.path.dirname(__file__))


# @app.route('/api/search', methods=['GET'])
# # FullMatrix[0] = uniqueTerms
# def dir():
#     query = request.args.get('query', default="", type=str)
#     [uniqueTerms, fullMatrix] = generateTermsFromFiles(basedir)
#     queryVector = generateQueryVector(query)
#     print(queryVector)
#     termsContainer = {
#         x: queryVector[x] if x in queryVector else 0 for x in uniqueTerms}
#     queryVector.update(termsContainer)
#     fullMatrix = updateTerms(fullMatrix, queryVector)
#     for i in range(1, len(fullMatrix)):
#         print(sim(queryVector, fullMatrix[i]))
#     # print('BBBBBBBBBBBBBBBBBBBBBBB')
#     # print(len(queryVector))
#     return json.dumps(fullMatrix[0])


@app.route('/api/basedir', methods=['GET'])
def what_ismy_basedir():
    return basedir


@app.route('/api/cerita/', methods=['GET'])
def hello_world():
    cerita = request.args.get('cerita', default="", type=str)
    data = open(os.path.join(basedir, 'static/'+cerita)).read()
    return data


@app.route("/api/upload", methods=['POST'])
def upload_files():
<<<<<<< HEAD
    print(request.data)
    dict_str = request.data.decode("UTF-8")
    mydata = ast.literal_eval(dict_str)
    print(mydata)
    if request.method == "POST":
        if request.data:
            files_html = mydata
            open(mydata['name'],'wb').write(request.data)
            return "DONE"
    return "DONE"
=======
    target = os.path.join(basedir + UPLOAD_DIRECTORY)
    if not os.path.isdir(target):
        os.mkdir(target)
    print("WOIIIIIIIIIIII")
    file = request.files['file']
    filename = secure_filename(file.filename)
    destination = "/".join([target, filename])
    file.save(destination)
    session['uploadFilePath'] = destination
    response = "apa aja dah"
    return response
>>>>>>> 10966bb5d148b1a42459c6da1b5e0f36843e26aa


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
