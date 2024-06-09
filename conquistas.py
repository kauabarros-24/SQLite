import sqlite3

conexao = sqlite3.connect('neps_sql_course.db')
cursor = conexao.cursor()

#Receber input's
iD = input()
name = input()
description = input()

#Primeira parte: Verficiar se o nome já existe
cursor.execute('SELECT name FROM achievement')
ok = False
for c in cursor.fetchall():
    if c[0] == name:
        ok = True
        break

if ok:
    print('invalid achivement')
else:
    cursor.execute('BEGIN')
    cursor.execute('UPDATE achievement SET name = ?, description = ? WHERE id = ?', (name, description, iD))
    conexao.commit()

cursor.close()
conexao.close()


