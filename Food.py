from tkinter import ttk
from tkinter import *
import customtkinter as ctk
import tkinter as tk


janela = tk.Tk()
janela.title('Wartale Foods')
janela.geometry('500x400')
janela.configure(background='white')
janela.resizable(True,True)
janela.wm_iconbitmap('wartale.ico')


dict = {'EXP': 'Beer: 2 Trigos e 2 Mardanos ou 2 Trigos e 2 Etheroot'
               'Fish Roll: 2 Trigos, 1 alga e 1 peixe'
            }

total_rows = len(dict)
total_columns = 3
class Table:

    def __init__(self, janela):

        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(janela, width=20, fg='blue',
                               font=('Arial', 16, 'bold'))

                self.e.grid(row=i, column=j)
                self.e.insert(END, dict[i][j])

def food(x=''):
    global dict
    atributo = x.upper()
    count = 0
    try:
        if atributo == "EXP":
            for i in dict.items():
                resp.configure(text=f'{dict["EXP"]}\n')


            for k in dict.items():
                for i in k:
                    print(f'{k}' ,end='')
                    print(f'{i}')
    except:
        resp.configure(text='Atributo não reconhecido, tente novamente!')



texto1 = ctk.CTkLabel(janela, text='Atributo:', corner_radius=100, bg_color='#000000')
texto1.grid(row=0, column=0, padx=10, pady=10)

etexto = ctk.CTkEntry(janela, width=40, corner_radius=100, bg_color='#000000')
etexto.grid(row=0, column=1, padx=10, pady=10)

button = ctk.CTkButton(janela, text='Buscar', hover_color='red',corner_radius=100, bg_color='#000000',
                       command=lambda: food(etexto.get()))
button.grid(row=1, column=1, padx=10, pady=10)

resp = tk.Table(janela,  text='', width=200, bg_color='red', fg_color='cyan')
resp.grid(row=2, column=1, padx=10, pady=10)









janela.mainloop()
