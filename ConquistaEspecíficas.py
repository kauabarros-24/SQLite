import sqlite3

conexao = sqlite3.connect('neps_sql_course.db')
cursor = conexao.cursor()

conquista = input()
cursor.execute("""
    SELECT user.username, achievement.name
    FROM user
    LEFT JOIN user_achievement ON user.id = user_achievement.user_id
    LEFT JOIN achievement ON user_achievement.achievement_id = achievement.id

""")


for c in cursor.fetchall():
    if c[1] == conquista:
        print(c[0], "achieved ")
    else:
        print(c[0], "not achieved")

cursor.close()
conexao.close()