from customtkinter import *

cont = 0.35
listText = []
listCheck = []

def checkBox_event(check_var, newTextBox, checkbox):
    if check_var.get() == "on":
        if newTextBox not in listText:
            listText.append(newTextBox)
            listCheck.append(checkbox)
    else:
        if newTextBox in listText:
            listText.remove(newTextBox)
            listCheck.remove(checkbox)

def buttonDelete_event():
    global cont

    for text in listText:
        text.destroy()
    for check in listCheck:
        check.destroy()

    cont -= 0.1 * len(listText)
    listText.clear()
    listCheck.clear()

def createTasks():
    global cont
    
    if cont < 0.749:
        newTextBox = CTkTextbox(master=app, width=500, height=10, font=("Arial", 18), corner_radius=10, fg_color="#3C3E40", border_color="#A6A486", border_width=1)
        check_var = StringVar(value="off")
        
        checkbox = CTkCheckBox(master=app, text="", fg_color="blue", checkbox_height=20, checkbox_width=20, width=1, variable=check_var, onvalue="on", offvalue="off")
        checkbox.configure(command=lambda cv=check_var, ntb=newTextBox, cb=checkbox: checkBox_event(cv, ntb, cb))

        newTextBox.insert("0.0", tasks.get())
        newTextBox.configure(state="disabled")
        newTextBox.place(relx=0.5, rely=cont, anchor="center")
        checkbox.place(relx=0.3, rely=cont, anchor="center")
        cont += 0.1

        tasks.delete(first_index=0, last_index=len(tasks.get()))
    else:
        print("Limite")

app = CTk()
app.geometry("500x400")

set_appearance_mode("dark")

textbox = CTkTextbox(master=app, text_color="white", width=400, height=100, font=("Arial", 40), fg_color="transparent")
tasks = CTkEntry(master=app, placeholder_text="Digite..", width=500, font=("Arial", 20), corner_radius=10)
button = CTkButton(master=app, text="Adicionar", corner_radius=50, fg_color="blue", command=createTasks, width=70, height=50, font=("Arial", 20), border_color="#A6A486", border_width=1, hover_color="#004F4D")
deletebutton = CTkButton(master=app, text="", corner_radius=100, fg_color="blue", command=buttonDelete_event, width=25, height=25)

textbox.insert("0.0", "Lista de tarefas")
textbox.configure(state="disabled")
textbox.place(relx=0.54, rely=0.1, anchor="center")
tasks.place(relx=0.5, rely=0.25, anchor="center")
button.place(relx=0.5, rely=0.8, anchor="center")
deletebutton.place(relx=0.29, rely=0.8, anchor="center")

app.mainloop()
