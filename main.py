#BIBLIOTECAS
import random
import smtplib
import email.message

#SERVIDOR FLASK
from flask import Flask, render_template, redirect 
from flask.globals import request

#MÓDULOS
from conexao import *

global idUsuario
global usuariosConectados
usuariosConectados = []

#Código principal
app = Flask(__name__)

#Renderizando menu inicial e outros
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
        return render_template('planner.html')

#Renderizando tela Task List
@app.route('/tasklist', methods = ["post", "get"])
def tasklist():
        return render_template("tasklist.html")

#Renderizando tela de atividades
@app.route('/atividades', methods = ["post", "get"])
def atividades():
        listarAtividades()
        return render_template("atividades.html", mostrar = dados)

#Renderização de recuperação de senha
@app.route('/recuperar', methods = ["post", "get"])
def recuperacao():
      return render_template("recuperar.html")

#VRenderizar codigo de acesso
@app.route('/codigoAcesso', methods = ['post', 'get'])
def codigoAcesso():
  return render_template("codigoAcesso.html")

#Cadastro e login de Usuário

#Redefinir senha
@app.route('/password', methods = ['post', 'get'])
def redefinir_password():
  return render_template("redefinirSenha.html")

#atualizar atividade
@app.route('/atualizarAtv', methods = ['post', 'get'])
def atualizar_Atividade():
  return render_template("atualizarAtv.html")
  
#Classe usuário
class Usuarios:
      def __init__(self, nomeUsuario, emailUsuario, senhaUsuario, usuarioID, conectado):
            self.nomeUsuario = nomeUsuario
            self.emailUsuario = emailUsuario
            self.senhaUsuario = senhaUsuario
            self.usuarioID = usuarioID
            self.conectado = conectado

      def getNome(self):
            return self.nomeUsuario

      def getEmail(self):
            return self.emailUsuario

      def getSenha(self):
            return self.senhaUsuario
        
      def getID(self):
            return self.usuarioID

      def usuarioOnline(self):
            return self.conectado
        
      def acessarInformacoesUsuario(self):
            informacoesUsuario = [self.nomeUsuario, self.emailUsuario, self.senhaUsuario, self.usuarioID, self.conectado]
            return informacoesUsuario

#Classe Atividade
class Atividade:
      def __init__(self, idAtividade, nomeAtividade, dataAtividade, descricaoAtividade):
          self.idAtividade = idAtividade
          self.nomeAtividade = nomeAtividade
          self.dataAtividade = dataAtividade
          self.descricaoAtividade = descricaoAtividade

      def acessarInformacoesAtividades(self):
          informacoesAtividades = [self.nomeAtividade, self.dataAtividade, self.descricaoAtividade]
          return informacoesAtividades
        
def receber_cadastro():
    try:
        conexao = iniciar_conexao()
        
        nome = request.form['nome']
        email = request.form['gmail']
        senha = request.form['senha']
      
        str(nome)
        str(email)
        str(senha)

        user = Usuarios(0,0,0,0,0)
        user.nomeUsuario = nome
        user.emailUsuario = email
        user.senhaUsuario = senha
        
        SQL_buscar_dados = "SELECT * FROM usuarios"
        aux = buscando_dados(conexao, SQL_buscar_dados)

      
        for index in range(len(aux)):
          for busca in range(4):
            lista = aux[index]

            if email == lista[busca]:
              var = "Cadastro já existente"
              return render_template("cadastro.html", resultado = var)
    
        SQL_inserir_usuario = "INSERT INTO usuarios(nome, email, senha) VALUES ('"+(nome)+"', '"+(email)+"', '"+(senha)+"')"
        inserir_usuario(conexao, SQL_inserir_usuario)

    
        return redirect('/')
      
    except:
      print('\033[1;49;31mErro ao realizar login de usuário.\033[m')

    return render_template("cadastro.html", resultado = "Erro ao realizar cadastro. Tente novamente.")
        
def realizar_login():
      try:
        conexao = iniciar_conexao()
        
        nome_login = request.form['username']
        senha_login = request.form['senha']
        
        str(nome_login)
        str(senha_login)
        
        SQL_buscar_dados = "SELECT * FROM usuarios"
        aux = buscando_dados(conexao, SQL_buscar_dados)
        
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
          return render_template("planner.html")

      except:
          print('\033[1;49;31mErro ao realizar login de usuário.\033[m')

      return render_template("login.html", erro = "Não foi possível validar os dados. Tente novamente.")
        
def validar_email():
      global confirmEmail 
      confirmEmail = False

      conexao = iniciar_conexao()
      
      emailRecuperar = request.form['email-recuperar']
      SQL_buscar_dados = "SELECT * FROM usuarios"
      active = buscando_dados(conexao, SQL_buscar_dados) 
      
      for index in range(len(active)):
          for busca in range(4):
            lista = active[index]
    
            if emailRecuperar == lista[busca]:
              confirmEmail = True
              
      if confirmEmail == True:
          codigoAcesso = random.randint(200,1000)
        
          SQL_buscar_nome = f"SELECT nome FROM usuarios WHERE email = {emailRecuperar}"
          nomeUsuario = buscando_dados(conexao, SQL_buscar_nome)
        
          corpo_email = f"""
          <body style="font-size: 16px; border: 2px solid #000; border-radius: 20px; color: #000;">  
            <p style="margin-left: 1rem;"><b>Olá usuário Vortex!</b><br>Você solicitou a recuperação de sua senha de acesso ao sistema Vortex. Seu código de acesso é:</p>
            <p style="color: #2f00ff; margin-left: 25rem;"><b>{codigoAcesso}<b></p>
            <h4 style="margin-left: 15rem;">
              <b>Insira o código de acesso no campo requerido.</b>
              <br><p style="margin-left: 1rem; margin-top: 1px;">Se não foi você, ignore esta mensagem.</p>
              <br><p style="margin-left: 1rem; font-size: 12px; font-style: italic; margin-top: 2px;">Este é um email automático, favor não responder.</p>
            </h4>
            <br><p style="margin-left: 1rem; font-size: 12px; font-style: italic; margin-top: 5px;">Atenciosamente, <br>Equipe Vortex</p>
        </<body>
          """
          
          msg = email.message.Message()
          msg['Subject'] = "Código de acesso - Planner Vortex"
          msg['From'] = 'suporte.pvortex@gmail.com'
          msg['To'] = f'{emailRecuperar}'
          password = 'yncjnzadbzofoggj' 
          msg.add_header('Content-Type', 'text/html')
          msg.set_payload(corpo_email )
          s = smtplib.SMTP('smtp.gmail.com: 587')
          s.starttls()
          s.login(msg['From'], password)
          s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
          print('Email enviado')

        
          conexao = iniciar_conexao()
          teste = str(codigoAcesso)
          inserir = "INSERT INTO codigos(codigo) VALUES ("+(teste)+")"
          inserir_usuario(conexao, inserir)
         
          return redirect("/codigoAcesso")
          
    
      else:
        return render_template("recuperar.html", resultado = "Email não encontrado. Tente novamente.")
      
      return redirect('/recuperar')

        
def adicionarAtividade():
    conexao = iniciar_conexao()

    nomeAtv = request.form['nomeAtv']
    dataAtv = request.form['dataAtv']
    descricaoAtv = request.form['descricaoAtv']

    str(nomeAtv)
    str(dataAtv)
    str(descricaoAtv)

    buscarID = f"SELECT id FROM usuarios WHERE nome  == '{user.nomeUsuario}'"
    idUsuario = buscando_dados(conexao, buscarID)
    user.usuarioID = idUsuario
  
    print(user.usuarioID)
  
    SQL_buscar_dados = f"INSERT INTO atividades(idUsuario, nomeAtividade, dataAtividade, descricaoAtividade) VALUES ('{user.nomeUsuario}', '{nomeAtv}', '{dataAtv}', '{descricaoAtv}')"

    atividade = inserir_atividade(conexao, SQL_buscar_dados)

  
    return redirect('atividades')
  
def listarAtividades():
    global dados
    conexao = iniciar_conexao()
  
    buscar_atividade = f"SELECT * FROM atividades WHERE idUsuario = '{user.nomeUsuario}'"
  
    dados = buscando_dados(conexao, buscar_atividade)
    print(dados)
    return dados


def excluirAtividade():
    try:
      conexao = iniciar_conexao()
      nomeAtividadeExcluir = request.form['nomeATV']
    
      buscar_atividade = f"DELETE FROM atividades WHERE nomeAtividade = '{nomeAtividadeExcluir}'"
      ativar = alterar_dados(conexao, buscar_atividade)
      return redirect('atividades')
      
    except:
      print("Não deu.")
      
    return render_template('atvidades.html', erro = "Não foi possível excluir a atividade.")

  
#Redefinir senha
@app.route('/redefinir', methods = ['post', 'get'])
def redefinir():
    conexao = iniciar_conexao()
  
    senhaNova = request.form['senha-redefinir']
    emailaux = request.form['emailvalido']
  
    emailUser = str(emailaux)
    
    buscar = "SELECT * FROM usuarios"
    aux = buscando_dados(conexao, buscar)
  
    for index in range(len(aux)):
      for busca in range(4):
        lista = aux[index]
        
        if emailUser == lista[busca]:
          confirmEmail = True
  
    if confirmEmail == True:
      atualizar = "UPDATE usuarios SET senha = '"+senhaNova+"'  WHERE email = '"+emailUser+"'"
      alterar_dados(conexao, atualizar) 
      return redirect("/login")
  
    return redirect("/password")

  
#Validar código de acesso
@app.route("/validarCodigo", methods = ['post', 'get'])
def validar_codigo():
    conexao = iniciar_conexao()
    
    codigo = request.form['codigo-email']
  
    buscar = "SELECT * FROM codigos"
    active = buscando_dados(conexao, buscar)
    var = 'Código inválido'
    for index in range(len(active)):
        for busca in range(1):
          lista = active[index]
  
          if codigo == lista[busca]:
            dropar = "DELETE FROM codigos WHERE codigo "
            deletar_tabela(conexao, dropar)
            return redirect('/password')
            
    
    return render_template('codigoAcesso.html', resultado = var)


  
#Função de cadastro de usuários
@app.route('/cadastrar', methods = ["post", "get"])
def recebe_cadastro():
  return  receber_cadastro()
  
#Função de validação de login
@app.route('/logar', methods = ["post", "get"])
def realiza_login():
  return realizar_login()
  
#Função validação de email
@app.route('/validar', methods = ["post", "get"])
def valida_email():
  return validar_email()
  
#Função de adicionar atividades
@app.route('/adicionar', methods = ["post", "get"])
def adiciona_atividade():
    return adicionarAtividade()

#Função de adicionar atividades
@app.route('/deletar', methods = ["post", "get"])
def exclui_atividade():
    return excluirAtividade()

  
#Criação de tabela no banco
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
      CREATE TABLE IF NOT EXISTS atividades(
      idAtividade integer PRIMARY KEY AUTOINCREMENT,
      nomeAtividade text NOT NULL,
      dataAtividade text NOT NULL,
      descricaoAtividade text NOT NULL,
      idUsuario integer,
      foreign key(idUsuario) references usuarios(id)
      );
    """

    criar_tabela(conexao, tabelaAtv)

def tabelaCodigos():
    conexao = iniciar_conexao()
  
    tabela_codigos =  """CREATE TABLE IF NOT EXISTS codigos(
      codigo text NOT NULL
      );
    """
    criar_tabela(conexao, tabela_codigos)
      
  
#Chamando funções
tabelaUsuarios()
tabelaAtividades()
tabelaCodigos()


user = Usuarios(0,0,0,0,0)

#Ativando servidor
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=True)

