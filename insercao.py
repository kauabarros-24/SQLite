import sqlite3 

conexao = sqlite3.connect('neps_sql_course.db')
cursor = conexao.cursor()

cursor.execute("""
    INSERT INTO achievement (name, description)
    VALUES ('Izi pizi', 'Solve 2 programming exercise')
""")


cursor.execute("""
    INSERT INTO achievement (name, description)
    VALUES ('Mastering in Python', 'Solve 5 programming exercise using Python')
""")

conexao.commit()


cursor.close()
conexao.close()