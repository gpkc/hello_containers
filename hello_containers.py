import socket

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/hello/<name>")
def hello(name):
    return jsonify({"message": f"Hello {name.capitalize()} from {socket.gethostname()}"})


if __name__ == '__main__':
    app.run()
