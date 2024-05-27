import sqlite3

#Conexao
conexao = sqlite3.connect('neps_sql_course.db')
cursor = conexao.cursor()

cursor.execute('SELECT title FROM programming_task ORDER BY users_solved')
resultados  = cursor.fetchall()
for c in resultados:
    print(resultados)

cursor.close()
conexao.close()