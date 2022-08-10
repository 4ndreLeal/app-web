from flask import Flask, render_template

app = Flask("hello")

@app.route("/")
def hello():
    return "Hello World"

@app.route("/contatos")
def contato():
    return render_template("index.html")