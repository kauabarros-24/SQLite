import sqlite3

conexao = sqlite3.connect('neps_sql_course.db')
cursor = conexao.cursor()

#Receber input:
tarefaID = int(input())

#SOMA DA TAREFA:
cursor.execute('SELECT programming_task_id, SUM(runtime), AVG(runtime), MAX(runtime) FROM submission WHERE programming_task_id = ?', (tarefaID, ))
for c in cursor.fetchall():
    print("{:.2f}\n{:.2f}\n{:.2f}".format(c[1], c[2], c[3]))
    
cursor.close()
conexao.close()