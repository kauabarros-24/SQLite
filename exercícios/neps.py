import sqlite3

#Conexão
conexao = sqlite3.connect('neps_sql_course(2).db')
cursor = conexao.cursor()

#Verificação de usuários
def verificar(nomeRecebido, nomeCadastro):
    return True if nomeCadastro == nomeRecebido else False


#Receber o nome de usuário
nome = input("Digite o nome de usuário: ")
encontrado = False

#Realizar consultas no db
cursor.execute('SELECT username FROM user')
usuarios = cursor.fetchall()

#Procurar
for nomes in usuarios:
    if verificar(nome, nomes):
        encontrado = True
        break

#Responder ao neps
print("S") if encontrado else print("N")

#Fechar conexão
cursor.close()
conexao.close() 
    


