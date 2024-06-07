import sqlite3

conexao = sqlite3.connect('neps_sql_course.db')
cursor = conexao.cursor()

#Receber input's:
iD = input(': ')
achievementName = input(': ')
description = input(': ')

#Fazer fazer consulta para validar:
cursor.execute('SELECT name, description FROM achievement')
ok = True
#Buscar dados
for c in cursor.fetchall():
    if achievementName == c[0] or description == c[1]:
        ok = False
        break

if ok == True:
    cursor.execute('UPDATE achievement SET id = ?, name = ?, description = ?', (iD, achievementName, description,))
    conexao.commit()
else:
    print('invalid achievement!')

cursor.close()
conexao.close()