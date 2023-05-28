# Import the necessary modules
import os
import sys
import json
import requests
from flask import Flask, render_template, request, jsonify

# Define the necessary functions
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)