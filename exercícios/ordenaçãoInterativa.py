import sqlite3

#Estabelecer conexão
conexao = sqlite3.connect('neps_sql_course.db')
cursor = conexao.cursor()

#Receber os input's
tipo = input()
ordem = input()

#Ordenar pela consulta:
if tipo == 'D':
    if ordem == "ASC":
        cursor.execute('SELECT title, difficulty, users_solved FROM programming_task ORDER BY difficulty')
    else:
        cursor.execute('SELECT title, difficulty, users_solved FROM programming_task ORDER BY difficulty DESC')
else:
    if ordem == "ASC":
        cursor.execute('SELECT title, difficulty, users_solved FROM programming_task ORDER BY users_solved')
    else:
        cursor.execute('SELECT title, difficulty, users_solved FROM programming_task ORDER BY users_solved DESC')

for c in cursor.fetchall():
    print(c[0], c[1], c[2])

cursor.close()
conexao.close()

