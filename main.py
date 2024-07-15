from customtkinter import * 

app = CTk()
app.geometry("500x400")

set_appearance_mode("dark")


checkbox = CTkCheckBox(master=app , text="",fg_color="blue",checkbox_height=20,checkbox_width=20)
tasks = CTkEntry(master=app , placeholder_text="Digite..",width=300)
button = CTkButton(master=app,text="Adicionar",corner_radius=50,fg_color="blue")



checkbox.place(relx=0.4,rely=0.25,anchor="center")
tasks.place(relx=0.5,rely=0.25,anchor="center")
button.place(relx=0.5,rely=0.7,anchor="center")
app.mainloop()