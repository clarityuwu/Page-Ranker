import requests
from flask import Flask, redirect, render_template, request, url_for
import json
import pageranker as pr

app = Flask(__name__)

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == 'POST':
        value = int(request.form.get('value', 0))
        return redirect(url_for('result', value=value))
    return render_template("index.html")

@app.route("/resultat/<int:value>", methods=("GET", "POST"))
def result(value):
    value = value * 100
    miniWeb = pr.genere_mini_web_aleatoire(10)
    fig1 = pr.affiche_visites_pages(miniWeb, 100, value)
    classement = pr.classement_pages(miniWeb, 100, value)
    fig2 = pr.affiche_mini_web(miniWeb, classement)
    fig1.savefig("static/result.png")
    fig2.savefig("static/result2.png")
    return render_template("resultat.html")

app.add_url_rule('/', 'index', index)
app.add_url_rule('/resultat/<int:value>', 'resultat', result, methods = ['GET'])