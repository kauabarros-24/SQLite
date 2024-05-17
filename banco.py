import sqlite3

#Conexão com o db:
conexao = sqlite3.connect('db.db')
cur = conexao.cursor()

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

usuarios = [
    ('Kaua', 'k@k.com', '1234'),
    ('Willin Bonner', 'bonner@william.com', '12345'),
    ('Ricardo Coração de leão', 'rei@cruzado.com', '1199')
]

# Executar a operação INSERT para cada usuário
cur.executemany("INSERT INTO user (email, name, password) VALUES (?, ?, ?)", usuarios)

# Confirmar as alterações no banco de dados
conexao.commit()

# Fechar o cursor e a conexão
cur.close()
conexao.close()