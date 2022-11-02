#Bibliotecas para Banco de Dados
import pandas as pd
import sqlite3
import json

#Criar database
arquivo = "./bd/banco.db"

#Comandos DDL e DML
def iniciar_conexao():
          conexao = None
          try:  
            conexao = sqlite3.connect(arquivo)
            print('\033[1;49;32mConexão bem sucedida.\033[m')

          except sqlite3.Error as var:
            print('\033[1;49;31mConexão mal sucedida.\033[m')



def fechar_conexao(conexao):
          if conexao:
            conexao.close()



def criar_tabela(conexao, SQL_criar_tabela):
          try:
            cursor = conexao.cursor()
            cursor.execute(SQL_criar_tabela)
            conexao.commit()
            print('\033[1;49;32mTabela criada com sucesso.\033[m')
  
          except sqlite3.Error as var:
            print('\033[1;49;31mComando mal sucedido.\033[m')

    

def inserir_usuario(conexao, SQL_inserir_usuario):
          try:
            cursor = conexao.cursor()
            cursor.exceute(SQL_inserir_usuario)
            print('\033[1;49;32mUsuário inserido com sucesso.\033[m')

          except sqlite3.Error as var:
            print('\033[1;49;31mComando mal sucedido.\033[m')




conexao = iniciar_conexao()