from flask import Flask, render_template, Response, request, redirect, url_for
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/forward/", methods=['POST'])
def move_forward():
    command = 'curl ' + '-s ' + 'localhost:5081/eeee'
    forward_message = os.popen(command).read()
    return render_template('index.html', forward_message=forward_message);

if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port=5080)