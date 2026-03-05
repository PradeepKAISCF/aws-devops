from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    # This is the "Healthy" version of the app
    return "<h1>GitOps Project Live on AWS! v1.0</h1>"

@app.route('/health')
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
