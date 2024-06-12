import sqlite3

conexao = sqlite3.connect('neps_sql_course.db')
cursor = conexao.cursor()

cursor.execute("""
   SELECT user.username, submission.solution
    FROM user
    INNER JOIN submission ON user.id = submission.user_id
""")
for c in cursor.fetchall():
    print(c)

cursor.close()
conexao.close()