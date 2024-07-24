import customtkinter as ctk
import tkinter as tk
import sqlite3
import banco
import automacao

class ToDoListApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("To-Do List")
        self.geometry("400x500")
        ctk.set_appearance_mode("dark")

        # Conectar ao banco de dados
        self.conn = sqlite3.connect('meu_banco_de_dados.db')
        self.cursor = self.conn.cursor()

        # Criar tabela se não existir (sem o campo concluida)
        # self.cursor.execute('DROP Tlucas fortunato
        #   Lista de tarefas pendentes  ABLE IF EXISTS tarefas')
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descricao TEXT NOT NULL
        )
        ''')
        self.conn.commit()
        

        # Lista de tarefas
        self.tasks = []

        # Frame principal
        self.frame = ctk.CTkFrame(self)
        self.frame.pack(padx=20, pady=20, fill='both', expand=True)

        # Entrada para novas tarefas
        self.entry = ctk.CTkEntry(self.frame, placeholder_text="Adicione uma nova tarefa")
        self.entry.pack(pady=(0, 10), fill='x')

        # Botão para adicionar tarefas
        self.add_button = ctk.CTkButton(self.frame, text="Adicionar", command=self.add_task)
        self.add_button.pack(pady=(0, 20))

        # Frame para as tarefas
        self.tasks_frame = ctk.CTkFrame(self.frame)
        self.tasks_frame.pack(fill='both', expand=True)

        # Botão para remover tarefas selecionadas
        self.remove_button = ctk.CTkButton(self.frame, text="Remover selecionadas", command=self.remove_tasks)
        self.remove_button.pack(pady=(10, 0))

        self.envia = ctk.CTkButton(self.frame, text="Enviar por email", command=self.envia_mail)
        self.envia.pack(pady=(10, 0))

        

        # Carregar tarefas do banco de dados
        self.load_tasks()

    def load_tasks(self):
        self.cursor.execute('SELECT * FROM tarefas')
        tarefas = self.cursor.fetchall()
        for tarefa in tarefas:
            task_var = tk.BooleanVar(value=False)
            task_check = ctk.CTkCheckBox(self.tasks_frame, text=tarefa[1], variable=task_var)
            task_check.pack(anchor='w', pady=5)
            self.tasks.append((task_check, task_var))

    def add_task(self):
        task_text = self.entry.get()
        if task_text:
            task_var = tk.BooleanVar()
            task_check = ctk.CTkCheckBox(self.tasks_frame, text=task_text, variable=task_var, corner_radius=5, height=5)
            task_check.pack(anchor='w', pady=5)
            self.tasks.append((task_check, task_var))
            self.entry.delete(0, tk.END)

            # Inserir a nova tarefa no banco de dados (sem o campo concluida)
            self.cursor.execute('''
            INSERT INTO tarefas (descricao)
            VALUES (?)
            ''', (task_text,))
            self.conn.commit()

    def remove_tasks(self):
        for task_check, task_var in self.tasks[:]:
            if task_var.get():
                # Remover do banco de dados
                self.cursor.execute('''
                DELETE FROM tarefas
                WHERE descricao = ?
                ''', (task_check.cget('text'),))
                self.conn.commit()
                
                task_check.destroy()
                self.tasks.remove((task_check, task_var))

    def envia_mail(self):
        tasks = banco.listaTarefas()
        if tasks:
                automacao.geraEmail(tasks)         
        

if __name__ == "__main__":
    
    app = ToDoListApp()
    app.mainloop()
