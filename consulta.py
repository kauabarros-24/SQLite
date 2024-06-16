import sqlite3

conexao = sqlite3.connect('neps_sql_course.db')
cursor = conexao.cursor()

cursor.execute("""
SELECT title
FROM programming_task
WHERE difficulty > (SELECT AVG(difficulty) FROM programming_task)
""")

for row in cursor.fetchall():
    print(row[0])

cursor.close()
conexao.close()