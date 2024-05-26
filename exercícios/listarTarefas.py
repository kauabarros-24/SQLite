import sqlite3
fila = {}

#Função para encontrar a dificuldade
def dificuldade(cur, dificuldade):
    #Realizar consulta
    cur.execute('SELECT title FROM programming_task WHERE difficulty <= ?', (dificuldade))

    #Iterar sobre as dificuldades
    for dificuldade in cur.fetchall():
        fila.add(dificuldade)

#Função para encontrar as resolvidas
def resolvidas(cur, resolvido):
    #Realizar consulta
    cur.execute('SELECT title FROM programming_task WHERE users_solved <= ?', (resolvido,))
    
    #Realizar consulta
    for titulo in cur.fetchall():
        fila.add(titulo)

#Conexão
conexao = sqlite3.connect('neps_sql_course.db')
cursor = conexao.cursor()

#Inputar
resolvida = input()
dificuldades = input()

#Passar para as funções
resolvidas(cursor, resolvida)
dificuldade(cursor, dificuldades)

#Resposta
while len(fila) >0:
    print(fila.remove())

cursor.close()
conexao.close()