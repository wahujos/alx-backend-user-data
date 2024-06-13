#!/usr/bin/env python3
"""
documenting the necessary imports
"""
from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def hello_world():
    """
    function to invoke
    """
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
