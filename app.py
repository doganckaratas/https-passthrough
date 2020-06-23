from flask import Flask, request, jsonify
import urllib.request

app = Flask(__name__)


@app.route('/', methods = ['GET'])
def root():
    try:
        param = request.args.get('url')
        resp = urllib.request.urlopen(param).read()
    except Exception:
        resp = {"error": "request failed.", "url" : param}

    return resp

if __name__ == '__main__':
    app.run(debug=True, threaded=True, port=8000)