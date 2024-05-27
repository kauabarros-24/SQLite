import sqlite3

#Função para realizar a consulta
def titulo(cur, nSolved, nDifficulty):
    #Realizar consulta:
    cur.execute('SELECT title FROM programming_task WHERE users_solved >= ? OR difficulty = ?', (nSolved, nDifficulty,))
    titulos = cur.fetchall()

    return [titulo[0] for titulo in titulos]

#Estabelecer conexão:
conexao = sqlite3.connect('neps_sql_course.db')
cursor = conexao.cursor()

#Inputar:
nResolvida = int(input())
nDificuldade = int(input())
titulos_resolvidos = titulo(cursor, nResolvida, nDificuldade)

for title in titulos_resolvidos:
    print(title)

cursor.close()
conexao.close()