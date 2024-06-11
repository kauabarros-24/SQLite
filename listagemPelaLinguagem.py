import sqlite3

con = sqlite3.connect("neps_sql_course.db")
cur = con.cursor()

language = input("Digite o nome da linguagem de programação: ")

cur.execute('SELECT ')
