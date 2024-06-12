import sqlite3

con = sqlite3.connect("neps_sql_course.db")
cur = con.cursor()

cur.execute('SELECT programming_task.id, submission.programming_task_id FROM programming_task INNER JOIN submission ON programming_task.id = submission.id')

cursor.