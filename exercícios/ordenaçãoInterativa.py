import sqlite3

conexao = sqlite3.connect('neps_sql_course.db')
cursor = conexao.cursor()

tipo = input(': ')
ordem = input(': ')

if tipo == 'U':
    if ordem == 'ASC':
        cursor.execute('SELECT title, difficulty, users_solved from programming_task ORDER BY users_solved ASC')
    else:
        cursor.execute('SELECT title, users_solved, difficulty FROM programming_task ORDER BY users_solved DESC')
else: 
    if ordem == 'ASC':
        cursor.execute('SELECT title, users_solved, difficulty FROM programming_task ORDER BY difficulty ASC')
    else:
        cursor.execute('SELECT title, users_solved, difficulty FROM programming_task ORDER BY difficulty DESC')
for c in cursor.fetchall():
    print(c)


cursor.close()
conexao.close()