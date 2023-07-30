import customtkinter as ctk
import tkinter

janela = ctk.CTk()
janela.title('Wartale Foods')
janela.geometry('500x400')
janela.configure(background='white')
janela.resizable(True,True)


texto = ctk.CTkLabel(janela, text='Atributo:',bg_color='white', fg_color='cyan',corner_radius=1000)
texto.grid(row=0, column=0, padx=10, pady=10)
etexto = ctk.CTkEntry(janela,bg_color='black',fg_color='red',)
etexto.grid(row=0, column=1, padx=1, pady=10)













janela.mainloop()
