import sqlite3


def check_username_exists(cur, username):
    #Pegar os dados do banco de dados:
    cur.execute("SELECT username FROM user")
    users = cur.fetchall()
    ok = False
    #Verificar a existência do username no na tabela
    for user in users:
        if user == username:
             ok = True
             break
    if ok == False:
        cur.execute("INSERT INTO (username) VALUES (?)", username)
    return ok

conexao = sqlite3.connect("neps_sql_course.db")
cur = conexao.cursor()
    
username = input()
if check_username_exists(cur, username):
    print("O usuário já existe")
else:
    print("O usuário não existe")

cur.close()
conexao.close()
