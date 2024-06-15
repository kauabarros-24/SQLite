import sqlite3

conexao = sqlite3.connect('neps_sql_course.db')
cursor = conexao.cursor()

cursor.execute("""
    SELECT u.username, s.solution
    FROM user AS u
    JOIN submission AS s ON u.id = s.user_id
""")

for c in cursor.fetchall():
    print(c)
