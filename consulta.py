import sqlite3

#Conexao
conexao = sqlite3.connect("db.db")
cursor = conexao.cursor()

cursor.execute("SELECT nome FROM vendedores")
nomeVendedores = cursor.fetchall()
for vendedores in nomeVendedores:
    print(vendedores)

cursor.close()
conexao.close