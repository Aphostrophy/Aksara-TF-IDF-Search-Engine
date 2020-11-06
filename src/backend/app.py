from flask import Flask, request
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

@app.route('/api', methods=['GET'])

def what_ismy_basedir():
    return basedir

@app.route('/api/cerita/', methods=['GET'])

def hello_world():
    cerita = request.args.get('cerita', default="", type=str)
    data = open(os.path.join(basedir,'static/'+cerita)).read()
    return data

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
