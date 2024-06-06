import sqlite3

conexao = sqlite3.connect('neps_sql_course.db')
cursor = conexao.cursor()

new_username = 'new_username'
user_id = 1

cursor.execute("""UPDATE user SET username = ? WHERE id = ?""", (new_username, user_id))

conexao.commit()

cursor.close()
conexao.close()