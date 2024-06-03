import sqlite3

conexao = sqlite3.connect('neps_sql_course.db')
cursor = conexao.cursor()

cursor.execute('SELECT programming_task_id, COUNT(*) AS num_submissions FROM submission GROUP BY programming_task_id')
for c in cursor.fetchall():
    print(c)
    
cursor.close()
conexao.close()