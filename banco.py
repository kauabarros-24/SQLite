import sqlite3

#Conexão com o db:
conexao = sqlite3.connect('db.db')
cursor = conexao.cursor()

#cursor.execute("""
#CREATE TABLE user(
#    id INTEGER PRIMARY KEY,
#    email TEXT NOT NULL UNIQUE,
#    name TEXT NOT NULL, 
#    password CHAR NOT NULL
#)
#""")

#cursor.execute("""
#CREATE TABLE produtos(
#    id INTEGER PRIMARY KEY,
#    nome_produto TEXT NOT NULL,
#    preco DECIMAL(10, 2)
#)
#""")

cursor.close()
conexao.close()