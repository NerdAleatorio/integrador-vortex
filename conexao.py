#Bibliotecas para Banco de Dados
import pandas as pd
import sqlite3


#CRIAR DATABASE
arquivo = "./bd/banco.db"

#Comandos DDL e DML
def iniciar_conexao():
        conexao = None
        try:  
          conexao = sqlite3.connect(arquivo)
          print('\033[1;49;32mConexão bem sucedida.\033[m')

        except sqlite3.Error as var:
          print('\033[1;49;31mConexão mal sucedida.\033[m')

        return conexao


def fechar_conexao(conexao):
        if conexao:
          conexao.close()
            

def criar_tabela(conexao, SQL_criar_tabela):
        try:
          cursor = conexao.cursor()
          cursor.execute(SQL_criar_tabela)
          print('\033[1;49;32mTabela criada com sucesso.\033[m')

        except sqlite3.Error as var:
          print('\033[1;49;31mComando mal sucedido.\033[m')


def inserir_usuario(conexao, SQL_inserir_usuario):
        try:
          cursor = conexao.cursor()
          cursor.execute(SQL_inserir_usuario)
          conexao.commit()
          print('\033[1;49;32mUsuário inserido com sucesso.\033[m')

        except sqlite3.Error as var:
          print('\033[1;49;31mComando mal sucedido.\033[m', var)

          
def buscando_dados(conexao, SQL_buscar_dados):
        dados = None
        try:
          cursor = conexao.cursor()
          cursor.execute(SQL_buscar_dados)
          dados = cursor.fetchall()
          print('\033[1;49;32mDados encontrados com sucesso.\033[m')
          
        except sqlite3.Error as var:
          print('\033[1;49;31mComando mal sucedido.\033[m', var)

        finally:
          return dados
        