from flask import Flask, request, redirect
import os

from flask.templating import render_template

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))


def dir():
    files = os.listdir('./static')
    D = []  # matriks kolom dari dokumen
    for elem in files:
        print(elem)
    return 'Files printed on console'


@app.route('/api', methods=['GET'])
def what_ismy_basedir():
    return basedir


@app.route('/api/cerita/', methods=['GET'])
def hello_world():
    cerita = request.args.get('cerita', default="", type=str)
    data = open(os.path.join(basedir, 'static/'+cerita)).read()
    return data


@app.route("/api/upload", methods=['GET', 'POST'])
def upload_files():
    if request.method == "POST":
        if request.files:
            files_html = request.files[files.name]
            print(files_html)
            return redirect(request.url)
    return render_template("static/upload.html")


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
