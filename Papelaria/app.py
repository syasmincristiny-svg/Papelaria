from flask import Flask 

app = Flask (__name__)

@app.route("/")
def inicio ():
    return "papelaria  ponto certo esta no ar !"

app.run (debug=True)

