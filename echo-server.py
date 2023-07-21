from flask import Flask
from flask import request
import sys
from markupsafe import escape

app = Flask(__name__)

@app.route("/<name>")
def hello(name):
    print(f"Call :: {name}")
    return f"Call :: {escape(name)}"

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5081)