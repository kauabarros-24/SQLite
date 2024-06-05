import sqlite3

conexao = sqlite3.connect('neps_sql_course.db')
cursor = conexao.cursor()

cursor.execute('''
CREATE TABLE user_rating(
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL UNIQUE,
    rating INTEGER NOT NULL,
    feedback TEXT,
    CHECK (rating >= 1 AND rating <= 5),
    FOREIGN KEY (user_id) REFERENCES user(id)  
)
''')

cursor.close()
conexao.close()