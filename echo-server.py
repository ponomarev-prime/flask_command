from flask import Flask
from flask import request
import sys
from markupsafe import escape

app = Flask(__name__)
#port = sys.argv[1];
port = 5081


@app.route("/<name>")
def hello(name):
    return f"Call :: {escape(name)}"


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=int(port))