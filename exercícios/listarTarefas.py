import sqlite3
from queue import SimpleQueue
fila = SimpleQueue()
def dificuldade(cur, dificuldade):
    cur.execute('SELECT title FROM programming_task WHERE difficulty = ?', (dificuldade,))
    dificuldades = cur.fetchall()
    for dificuldade in dificuldades:
        fila.put(dificuldade[0])
def resolvidas(cur, resolvido):
    cur.execute('SELECT title FROM programming_task WHERE users_solved = ?', (resolvido,))
    titulos = cur.fetchall()
    for titulo in titulos:
        fila.put(titulo[0])
conexao = sqlite3.connect('neps_sql_course.db')
cursor = conexao.cursor()
resolvida = input("Número de resoluções: ")
dificuldades = input("Dificuldade: ")
resolvidas(cursor, resolvida)
dificuldade(cursor, dificuldades)
while not fila.empty():
    print(fila.get())
cursor.close()
conexao.close()
