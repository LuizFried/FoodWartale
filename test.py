from tkinter import ttk
from tkinter import *
import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox


janela = tk.Tk()
janela.title('Wartale Foods')
janela.geometry('580x300')
janela.configure(background='#000000')
janela.resizable(True,True)
janela.wm_iconbitmap('wartale.ico')


lst = list()
total_rows = 1
total_columns = 1


def lista():
    global lst
    if atributo == 'EXP':
        lst = [('Nut Crusted Fish', '2-Ambernut', '2-Lemodine', '', ''),
       ('Nut Crusted Fish', '2-Ambernut', '2-Abysscarp', '', ''),
       ('Rossted Ambernut', '4-Ambernut', '', '', ''),
       ('Steamed fish', '4-Lemodine', '', '', ''),
       ('Steamed fish', '4-Abysscarp', '', '', ''),
       ('Glazed fish', '2-Royaljelly', '2-Lemodine', '', ''),
       ('Glazed fish', '2-Royaljelly', '2-Claret', '', '')]



class Table:

    def __init__(self, f1):

        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(f1, width=15, fg='#091174',bg='#c4c8c5',
                               font=('Arial', 10, 'bold'))

                self.e.grid(row=i+2, column=j, padx=2, pady=5)
                self.e.insert(END, lst[i][j])

def food(x=''):
    global dict, atributo, total_rows, total_columns
    atributo = x.upper()

    try:
        if atributo == "EXP":
            lista()
            total_rows = len(lst)
            total_columns = len(lst[0])
            resp = Table(f1)

    except:
        messagebox.showerror('ERRO','Atributo não reconhecido, tente novamente!')


f0 = ctk.CTkFrame(janela, bg_color='#000000', fg_color='#000000')
f0.grid(row=0, column=0, columnspan=3)
texto1 = ctk.CTkLabel(f0, text='Atributo:',width=150, corner_radius=100,fg_color='#091174',text_color='white',
                      bg_color='#000000')
texto1.grid(row=0, column=0, padx=2, pady=10)

etexto = ctk.CTkEntry(f0, width=200, corner_radius=100, bg_color='#000000')
etexto.grid(row=0, column=1, padx=2, pady=10)

button = ctk.CTkButton(f0,width=200, text='Buscar', hover_color='red',corner_radius=100, bg_color='#000000',
                       command=lambda: food(etexto.get()))
button.grid(row=0, column=2, padx=2, pady=10)

f1 = ctk.CTkFrame(janela, bg_color='#000000', fg_color='#000000')
f1.grid(row=2, column=0, columnspan=total_columns, rowspan=total_rows)

janela.mainloop()