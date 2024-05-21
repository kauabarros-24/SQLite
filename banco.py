import sqlite3

#Conexão:
conexao = sqlite3.connect("db.db")
cursor = conexao.cursor()

#Tabelas

#cursor.execute("""
#CREATE TABLE compradores(
#    id INTEGER PRIMARY KEY,
#    nome CHAR NOT NULL,
#    email CHAR NOT NULL UNIQUE
#)
#""")

#cursor.execute("""
#CREATE TABLE vendedores(
#    id INTEGER PRIMARY KEY,
#    nome CHAR NOT NULL,
#    email CHAR NOT NULL unique 
#)
#""")

#cursor.execute("""
#CREATE TABLE PRODUTOS(
#    id INTEGER PRIMARY KEY,
#    nome CHAR NOT NULL,
#    preco DECIMAL(10, 2) NOT NULL,
#    FOREIGN KEY (id) REFERENCES vendedores (id)
#)               
#""")

#Popular o banco de dados

users = [
    (1, "Kaua", "K@k.com"),
    (2, "Willian Bonner", "w@b.com"),
    (3, "Osvaldo", "o@s.com")
]

vendedores = [
    (1, "Olavo", "o@l.com")
]

produtos = [
    (1, "Calça", 10.46)
]

#Inserir dados nas tabelas
cursor.executemany("INSERT INTO compradores (id, nome, email) VALUES (?, ?, ?)", users)
cursor.executemany("INSERT INTO vendedores (id, nome, email) VALUES (?, ?, ?)", vendedores)
cursor.executemany("INSERT INTO produtos (id, nome, preco) VALUES (?, ?, ?)", produtos)

conexao.commit()

cursor.close()
conexao.close()
