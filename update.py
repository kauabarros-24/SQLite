import sqlite3

conexao = sqlite3.connect('neps_sql_course.db')
cursor = conexao.cursor()

cursor.execute('BEGIN')

try:
    cursor.execute("INSERT INTO (name) VALUES (conquistador)")
    cursor.execute("INSERT INTO user_achievement(user_id, achievement_id) VALUES (1, 3)")
    conexao.commit()
except:
    conexao.rollback()

cursor.close()
conexao.close()