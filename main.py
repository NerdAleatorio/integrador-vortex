#Bibliotecas
from flask import Flask, render_template, redirect 
from flask.globals import request
from usuario import *
from conexao import *



#Código principal
app = Flask(__name__)


@app.route('/')
def index():
          return render_template("index.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)
