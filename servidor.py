
from flask import Flask, app
from random import randint

app=Flask(__name__)
#numero elegido aleatoriamente
aleatorio=randint(0,9)
print(aleatorio)

@app.route("/")
def home():
    return "<h1>Adivina un número entre en 0 y 9</h1>\
    <img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>"

@app.route("/<int:adivinado>")
def adivinando(adivinado):
    if adivinado<aleatorio:
        return "<h1 style='color:red;'>Demasiado bajo, intenta de nuevo!!!</h1>\
            <img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
    elif adivinado>aleatorio:
        return "<h1 style='color:blue;'>Demasiado alto, intenta de nuevo!!!</h1>\
            <img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"
    else:
        return f"<h1 style='color:green;'>Correcto, soy el {aleatorio}!!!</h1>\
            <img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"

if __name__=="__main__":
    app.run(debug=True)