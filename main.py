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


@app.route('/cadastro', methods = ["post", "get"])
def cadastro():
          return render_template("cadastro.html")


@app.route('/login', methods = ["post", "get"])
def login():
          return render_template("login.html")

@app.route('/planner', methods = ["post", "get"])
def planner():
          return render_template("planner.html")

@app.route('/conta', methods = ["post", "get"])
def conta():
          return render_template("conta.html")



@app.route('/tasklist', methods = ["post", "get"])
def tasklist():
          return render_template("tasklist.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=True)
