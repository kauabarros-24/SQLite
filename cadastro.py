import sqlite3

conexao = sqlite3.connect('neps_sql_course.db')
cursor = conexao.cursor()

username = input()
email = input()
birthdate = input()
lista = [username, email, birthdate]

try:
    cursor.execute('INSERT INTO user(username, email, birthdate) VALUES (?, ?, ?)', lista)
    conexao.commit()
except sqlite3.IntegrityError:
    print('invalid user')
    
conexao.commit()

cursor.close()
conexao.close()