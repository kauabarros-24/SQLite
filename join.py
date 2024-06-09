import sqlite3

conexao = sqlite3.connect('neps_sql_course.db')
cursor = conexao.cursor()

cursor.execute('SELECT username FROM user UNION SELECT name FROM achievement')
for c in cursor.fetchall():
    print(c[0])

cursor.close()
conexao.close()