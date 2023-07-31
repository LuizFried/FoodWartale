from tkinter import ttk
from tkinter import *
import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox


janela = tk.Tk()
janela.title('Wartale Foods')
janela.geometry('580x300')
janela.configure(background='#000000')
janela.resizable(False,False)
janela.wm_iconbitmap('wartale.ico')


lst = [('Beer', '2-Trigos', '2-Mardanos', '', ''),
       ('Beer', '2-Trigos', '2-Etheroot', '', ''),
       ('Fish Roll', '2-Trigos', '1-Alga', '1-Peixe', ''),
       ('Thalon Wine', '2-Trigos', '2-Miragewort', '', ''),
       ('Wyzen Mead', '2-Trigos', '2-Royaljelly', '', '')]


total_rows = len(lst)
total_columns = len(lst[0])
class Table:

    def __init__(self, janela):

        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(janela, width=15, fg='#091174',bg='#c4c8c5',
                               font=('Arial', 10, 'bold'))

                self.e.grid(row=i+2, column=j, padx=2, pady=5)
                self.e.insert(END, lst[i][j])

def food(x=''):
    global dict
    atributo = x.upper()

    try:
        if atributo == "EXP":
            resp = Table(janela)

    except:
        messagebox.showerror('ERRO','Atributo não reconhecido, tente novamente!')



texto1 = ctk.CTkLabel(janela, text='Atributo:', corner_radius=100,fg_color='#091174',text_color='white',
                      bg_color='#000000')
texto1.grid(row=0, column=0, padx=2, pady=10)

etexto = ctk.CTkEntry(janela, width=100, corner_radius=100, bg_color='#000000')
etexto.grid(row=0, column=1, padx=2, pady=10)

button = ctk.CTkButton(janela,width=100, text='Buscar', hover_color='red',corner_radius=100, bg_color='#000000',
                       command=lambda: food(etexto.get()))
button.grid(row=0, column=2, padx=2, pady=10)












janela.mainloop()
