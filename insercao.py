import sqlite3 

conexao = sqlite3.connect('neps_sql_course.db')
cursor = conexao.cursor()

values = [(1,1), (2, 1), (3, 1)]

cursor.executemany("""INSERT INTO user_achievement (user_id, achievement_id) VALUES (?, ?)""", values)

conexao.commit()


cursor.close()
conexao.close()