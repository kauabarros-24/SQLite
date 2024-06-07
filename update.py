import sqlite3

conexao = sqlite3.connect('neps_sql_course.db')
cursor = conexao.cursor()

user_id = 1

cursor.execute('DELETE FROM user WHERE id = ?', (user_id,))

conexao.commit()

cursor.close()
conexao.close()