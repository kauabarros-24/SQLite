import sqlite3

conexao = sqlite3.connect('neps_sql_course.db')
cursor = conexao.cursor()

username = "bob' OR 1 = 1;--"

cursor.execute(f"""SELECT * FROM user WHERE username = '{username}'""")

nomes = cursor.fetchall()
print(nomes)