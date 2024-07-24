import sqlite3

conn = sqlite3.connect('meu_banco_de_dados.db')
cursor = conn.cursor()

def listaTarefas():
    cursor.execute('SELECT * FROM tarefas')
    tarefas = cursor.fetchall()
    for tarefa in tarefas:
        print(tarefa[1])
    return [tarefa[1] for tarefa in tarefas]
    
    



    

