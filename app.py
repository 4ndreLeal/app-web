from flask import Flask

app = Flask("hello")

@app.route("/")
def hello():
    return "Hello World"

@app.route("/contatos")
def contato():
    return """<html>
                    <head>
                        <title>Contatos</title>
                    </head>
                    <body>
                        <h1>André Pinheiro Leal</h1>
                        <h2>andre@email.com</h2>
                        <h3>8699887-7665</h3>
                    </body>
                </html>"""