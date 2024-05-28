import sqlite3

#Conexao
conexao = sqlite3.connect('neps_sql_course.db')
cursor = conexao.cursor()

cursor.execute('SELECT title, difficulty FROM programming_task ORDER BY difficulty')
for c in cursor.fetchall():
    print(c)

cursor.close()
conexao.close()