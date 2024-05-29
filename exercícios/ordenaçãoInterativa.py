import sqlite3

#Conexão com o banco de dados
conexao = sqlite3.connect('neps_sql_course_db')
cursor = conexao.cursor()

#Inputar
tipo = input(": ")
ordem = input(": ")

if tipo == "U":
    cursor.execute('SELECT title, difficulty, users_solved, COUNT(user_solved) AS num_users FROM programming_task GROUP BY num_users ASC') if ordem == "ASC" else cursor.execute('SELECT title, difficulty, users_solved, COUNT(user_solved) AS num_users FROM programming_task GROUP BY num_users ASC')
else:
    cursor.execute('SELECT title, difficulty, users_solved, COUNT(difficulty) AS num_users FROM programming Task GROUP BY num_users ASC') if ordem == "ASC" else cursor.execute('SELECT title, difficulty, users_solved, COUNT(difficulty) AS num_users FROM programming Task GROUP BY num_users DESC')

for c in cursor.fetchall():
    print(c[0], c[1],c[2], end='\n')

cursor.close()
conexao.close()