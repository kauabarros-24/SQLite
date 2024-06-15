import sqlite3

conexao = sqlite3.connect('neps_sql_course.db')
cursor = conexao.cursor()

#Receber os inputs     
linguagem = input()

cursor.execute("""
SELECT programming_task.title
FROM programming_task
JOIN submission ON programming_task.id = submission.programming_task_id
WHERE submission.programming_language = ?
ORDER BY programming_task.id
""", (linguagem, ))

for c in cursor.fetchall():
    print(c[0])

cursor.close()
conexao.close()