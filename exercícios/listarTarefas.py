import sqlite3

# Set para armazenar os títulos das tarefas
titles = set()

# Função para encontrar a dificuldade
def dificuldade(cur, dificuldade):
    # Realizar consulta
    cur.execute('SELECT title FROM programming_task WHERE difficulty = ?', (dificuldade,))
    
    # Iterar sobre as dificuldades
    for titulo in cur.fetchall():
        titles.add(titulo[0])  # Adicionar título ao conjunto

# Função para encontrar as resolvidas
def resolvidas(cur, resolvido):
    # Realizar consulta
    cur.execute('SELECT title FROM programming_task WHERE users_solved = ?', (resolvido,))
    
    # Iterar sobre os títulos resolvidos
    for titulo in cur.fetchall():
        titles.add(titulo[0])  # Adicionar título ao conjunto

# Conexão
conexao = sqlite3.connect('neps_sql_course.db')
cursor = conexao.cursor()

# Input
resolvida = input("Quantidade de resolvidos: ")
dificuldades = input("Dificuldade mínima: ")

# Passar para as funções
resolvidas(cursor, resolvida)
dificuldade(cursor, dificuldades)

# Resposta
for titulo in titles:
    print(titulo)

cursor.close()
conexao.close()
