import requests
from flask import Flask, redirect, render_template, request, url_for
import json

app = Flask(__name__)

@app.route("/", methods=("GET", "POST"))
def index():
    return render_template('index.html')

app.add_url_rule('/', 'index', index)