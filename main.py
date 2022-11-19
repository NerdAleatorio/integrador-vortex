 #BIBLIOTECAS
from conexao import *

#SERVIDOR FLASK
from flask import Flask, render_template, redirect 
from flask.globals import request

#Código principal
app = Flask(__name__)
 
#Renderizando menu inicial
@app.route('/')
def index():
      return render_template("index.html")
      
#Renderizando tela de cadastro
@app.route('/cadastro', methods = ["post", "get"])
def cadastro():
      return render_template("cadastro.html")
  
#Renderizando tela de login
@app.route('/login', methods = ["post", "get"])
def login():
      return render_template("login.html")

#Renderizando tela do planner
@app.route('/planner', methods = ["post", "get"])
def planner():
        return render_template("planner.html")

#Renderizando tela de calendário
@app.route('/calendario', methods = ['post', 'get'])
def calendario():
        return render_template("calendario.html")


#Renderizando tela Task List
@app.route('/tasklist', methods = ["post", "get"])
def tasklist():
        return render_template("tasklist.html")


#Renderizando tela de atividades
@app.route('/atividades', methods = ["post", "get"])
def atividades():
        return render_template("atividades.html")


#Função de cadastro de usuários
@app.route('/cadastrar', methods = ["post", "get"])
def receber_cadastro():
  try:
      conexao = iniciar_conexao()
      
      nome = request.form['nome']
      email = request.form['gmail']
      senha = request.form['senha']

      username = nome
      emailuser = email
      senhauser = senha
  
      str(username)
      str(emailuser)
      str(senhauser)
      
      print(nome, email, senha)
      
      SQL_inserir_usuario = "INSERT INTO usuarios(nome, email, senha) VALUES ('"+(username)+"', '"+(emailuser)+"', '"+(senhauser)+"')"
      inserir_usuario(conexao, SQL_inserir_usuario)
      
      return redirect('/')
  except:
      print('\033[1;49;31mErro ao realizar login de usuário.\033[m')

  return render_template("cadastro.html")
  
#Função de validação de login
@app.route('/logar', methods = ["post", "get"])

def realizar_login():
  try:
      conexao = iniciar_conexao()
      global nome_login
      nome_login = request.form['username']
      senha_login = request.form['senha']

      global nome_user
      nome_user = nome_login

      str(nome_login)
      str(senha_login)

      print(nome_login, senha_login)

      SQL_buscar_dados = "SELECT * FROM usuarios"
      aux = buscando_dados(conexao, SQL_buscar_dados)
      print(aux)
    
      for index in range(len(aux)):
        for busca in range(4):
          lista = aux[index]

          if nome_login == lista[busca]:
            confirmNome = True

      for index in range(len(aux)):
        for busca in range(4):
          lista = aux[index]
          if senha_login == lista[busca]:
            confirmPass = True
  
            
      if confirmPass == True and confirmNome == True: 
        return render_template('planner.html', nome_user = nome_login)

  except:
      print('\033[1;49;31mErro ao realizar login de usuário.\033[m')

  return render_template("login.html", erro = "Não foi possível validar os dados. Tente novamente.")


#Função de recuperação de senha
@app.route('/recuperar', methods = ["post", "get"])
def recuperar_senha():
  return render_template("recuperar.html")
  
#Criar tabela usuário
def tabelaUsuarios():
    conexao = iniciar_conexao()
  
    tabela = """
      CREATE TABLE IF NOT EXISTS usuarios(
      id integer PRIMARY KEY AUTOINCREMENT,
      nome text NOT NULL,
      email text NOT NULL,
      senha text NOT NULL
      );
    """
    criar_tabela(conexao, tabela)

def tabelaAtividades():
    conexao = iniciar_conexao()

    tabelaAtv = """
      CREATE TABLE IF NOT EXISTS usuarios(
      idAtividade integer PRIMARY KEY AUTOINCREMENT,
      nomeAtividade text NOT NULL,
      dataAtividade text NOT NULL,
      descricaoAtividade text NOT NULL
      );
    """

    criar_tabela(conexao, tabelaAtv)
  
#Chamando funções
tabelaUsuarios()

  
#Ativando servidor
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=True)

