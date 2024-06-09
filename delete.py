import sqlite3

conexao = sqlite3.connect('neps_sql_course.db')
cursor = conexao.cursor()

#Receber ID
iD = input()

#Verificar se o valor já existe
ok = False
try:
    cursor.execute('SELECT id FROM achievement WHERE id = ?', (iD))
except sqlite3.ProgrammingError:
    ok = True

if ok:
    print('invalid achievement')
else:
    cursor.execute('BEGIN')
    cursor.execute('DELETE FROM achievement WHERE id = ?', (iD))
    conexao.commit()


cursor.close()
conexao.close()