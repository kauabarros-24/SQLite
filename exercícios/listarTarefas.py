import sqlite3
from queue import SimpleQueue

#Conexão com o banco de dados:
conexao = sqlite3.connect('neps_sql_course.db')
cursor = conexao.cursor()
fila = SimpleQueue()

#Função da dificuldade

#Função para às resolvidas
def resolvidas(cursor, resolvidas):
    #Acessar a fila de fora
    global fila

    #Realizar consulta:
    cursor.execute(f'SELECT title FROM programming_task WHERE = {resolvidas}"')
    solvedNumber = cursor.fetchall()

    #Buscar
    for solved in solvedNumber:
        fila.put(solved)

    return fila
    


#Função para listar tarefas
def listarTarefas(cursor, resolvidas, dificuldade):

    #Passar para resolvidas
    resolvidas(cursor, resolvidas)
    

#Pegar do "inputador"
resolvidas = int(input("R: "))
dificuldade = int(input("D: "))

#Passar para a função principal
listarTarefas(cursor, resolvidas, dificuldade)





