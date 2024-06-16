import sqlite3

conexao = sqlite3.connect('neps_sql_course.db')
cursor = conexao.cursor()

cursor.execute("""
SELECT username
FROM user
WHERE id IN (
    SELECT DISTINCT user_id
    FROM submission

)

            
""")

for c in cursor.fetchall():
    print(c)
cursor.close()
conexao.close()