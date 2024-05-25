import sqlite3

# Função para verificar o usuário
def check_username_exists(cur, username):
    # Realizar a consulta
    cur.execute('SELECT username FROM user')
    usuarios = cur.fetchall()
    # Buscar
    for nome in usuarios:
        # Caso o usuário seja encontrado, retornará verdadeiro
        if username == nome[0]:
            return True
    return False

if __name__ == "__main__":
    # Conexão
    con = sqlite3.connect("neps_sql_course.db")
    cur = con.cursor()

    # Pegar o nome de usuário
    username = input()

    print("S") if check_username_exists(cur, username) else print("N")

    cur.close()
    con.close()
