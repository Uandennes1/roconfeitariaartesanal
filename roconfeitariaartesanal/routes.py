from flask import render_template
from roconfeitariaartesanal import app


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/bolos')
def bolos():
    return render_template('bolos.html')

@app.route('/sobremesas')
def sobremesas():
    return render_template('sobremesas.html')

@app.route('/salgados')
def salgados():
    return render_template('salgados.html')
