import sqlite3

conn = sqlite3.connect('meu_banco_de_dados.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM tarefas')
tarefas = cursor.fetchall()

for tarefa in tarefas:
    print(tarefa)

conn.close()


    

