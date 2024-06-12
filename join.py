import sqlite3

conexao = sqlite3.connect('neps_sql_course.db')
cursor = conexao.cursor()

cursor.execute('SELECT programming_task.id, submission.programming_task_id FROM programming_task INNER JOIN submission ON programming_task.id = submission.id')
for c in cursor.fetchall():
    print(c)

cursor.close()
conexao.close()