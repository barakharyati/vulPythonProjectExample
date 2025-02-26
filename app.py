# app.py
import flask
import yaml  # Known for arbitrary code execution vulnerabilities in unsafe_load
import requests  # Potential vulnerabilities in old versions

app = flask.Flask(__name__)

@app.route('/')
def home():
    return "Hello, this is a vulnerable app!"

@app.route('/config', methods=['POST'])
def config():
    data = flask.request.data.decode('utf-8')
    try:
        config = yaml.safe_load(data)  # Safe, but unsafe_load is vulnerable
        return flask.jsonify(config)
    except Exception as e:
        return str(e), 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
