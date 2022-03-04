from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'claveSecreta'

@app.route('/')
def index():
    session.clear()
    return render_template("index.html")

@app.route('/process',methods=['POST'])
def process():
    session['informacion'] = request.form
    return redirect("/result")

@app.route('/result')
def result():
    request.form = session['informacion']
    print(request.form)
    return render_template("show.html",nombre = request.form['txt_nombre'], lugar = request.form['optionCiudad'], 
    lenguaje = request.form['optionLenguaje'], comentarios= request.form['txt_comentario'])

if __name__=="__main__":
    app.run(debug=True)