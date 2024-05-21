import sqlite3

#Conexao
conexao = sqlite3.connect("db.db")
cursor = conexao.cursor()

#cursor.execute("SELECT nome FROM vendedores")
#nomeVendedores = cursor.fetchall()
#for vendedores in nomeVendedores:
#    print(vendedores)

cursor.execute("SELECT nome FROM vendedores WHERE id = 1")

user1 = cursor.fetchone()

if user1:
    print(user1)
else:
    print("Usuário não encontrado")

cursor.close()
conexao.close