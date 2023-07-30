import customtkinter as ctk
import tkinter as tk


janela = tk.Tk()
janela.title('Wartale Foods')
janela.geometry('500x400')
janela.configure(background='#000000')
janela.resizable(True,True)


texto = ctk.CTkLabel(janela, text='Atributo:', bg_color='#000021', fg_color='green', corner_radius=100,
                     font=('Monument Extended', 13, 'bold'))
texto.grid(row=0, column=0, padx=10, pady=10)
etexto = ctk.CTkEntry(janela, bg_color='black', fg_color='grey', font=('Monument Extended', 13, 'bold'),
                      corner_radius=100,width=200)
etexto.grid(row=0, column=1, padx=1, pady=10, sticky='nwse')

button = ctk.CTkButton(janela,text='Buscar', fg_color='Gold', bg_color='#000000', corner_radius=100,
                       text_color='black', width=70,
                       font=('Monument Extended', 13, 'bold'))
button.grid(row=0, column=4, padx=10, pady=10)












janela.mainloop()
