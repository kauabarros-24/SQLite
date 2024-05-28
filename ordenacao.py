import sqlite3

#Conexao
conexao = sqlite3.connect('neps_sql_course.db')
cursor = conexao.cursor()

cursor.execute('SELECT programming_task_id, AVG(runtime) AS avg_media_time FROM submission GROUP BY programming_task_id HAVING avg_media_time > 0.1')

for c in cursor.fetchall():
    print(c[0], "id -", f"{c[1]}s")
cursor.close()
conexao.close()