from flask import Flask, request
from flask_cors import CORS
from Matrixterm import generateTermsFromFiles, generateQueryVector, updateTerms
from vectorizer import sim
import os
import json

from flask.templating import render_template

app = Flask(__name__)
CORS(app)
basedir = os.path.abspath(os.path.dirname(__file__))


@app.route('/api/search', methods=['GET'])
# FullMatrix[0] = uniqueTerms
def dir():
    query = request.args.get('query', default="", type=str)
    [uniqueTerms, fullMatrix] = generateTermsFromFiles(basedir)
    queryVector = generateQueryVector(query)
    print(queryVector)
    termsContainer = {
        x: queryVector[x] if x in queryVector else 0 for x in uniqueTerms}
    queryVector.update(termsContainer)
    fullMatrix = updateTerms(fullMatrix, queryVector)
    for i in range(1, len(fullMatrix)):
        print(sim(queryVector, fullMatrix[i]))
    # print('BBBBBBBBBBBBBBBBBBBBBBB')
    # print(len(queryVector))
    return json.dumps(fullMatrix[0])


@app.route('/api/basedir', methods=['GET'])
def what_ismy_basedir():
    return basedir


@app.route('/api/cerita/', methods=['GET'])
def hello_world():
    cerita = request.args.get('cerita', default="", type=str)
    data = open(os.path.join(basedir, 'static/'+cerita)).read()
    return data


# @app.route("/api/upload", methods=['GET', 'POST'])
# def upload_files():
#     if request.method == "POST":
#         if request.files:
#             files_html = request.files[files.name]
#             print(files_html)
#             return redirect(request.url)
#     return render_template("static/upload.html")


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
