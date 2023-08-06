from tkinter import ttk
from tkinter import *
import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox


janela = tk.Tk()
janela.title('Wartale Foods')
janela.geometry('590x300')
janela.configure(background='#000000')
bg = PhotoImage(file = "imagemdefundo.png")
label1 = Label(janela, image = bg)
label1.place(x=0, y=0)
janela.resizable(False,False)
janela.wm_iconbitmap('wartale.ico')


lst = list()
total_rows = 1
total_columns = 1
atrib = ['EXP','ABS','ATK']

def lista():
    global lst
    if atributo == 'EXP':
        lst = [('Beer', '2-Trigos', '2-Mardanos', '', ''),
       ('Beer', '2-Trigos', '2-Etheroot', '', ''),
       ('Fish Roll', '2-Trigos', '1-Alga', '1-Peixe', ''),
       ('Thalon Wine', '2-Trigos', '2-Miragewort', '', ''),
       ('Wyzen Mead', '2-Trigos', '2-Royaljelly', '', '')]

    if atributo == 'ATK':
        lst = [('Nut Crusted Fish', '2-Ambernut', '2-Lemodine', '', ''),
       ('Nut Crusted Fish', '2-Ambernut', '2-Abysscarp', '', ''),
       ('Rossted Ambernut', '4-Ambernut', '', '', ''),
       ('Steamed fish', '4-Lemodine', '', '', ''),
       ('Steamed fish', '4-Abysscarp', '', '', ''),
       ('Glazed fish', '2-Royaljelly', '2-Lemodine', '', ''),
       ('Glazed fish', '2-Royaljelly', '2-Claret', '', '')]

    if atributo == 'ABS':
        lst = [('Carrot stew', '2-Milk', '2-Carrot', '', ''),
               ('Bread', '2-Ambernut', '2-Trigos', '', ''),
               ('Bread', '4-Trigos', '', '', ''),
               ('Bread', '1-Ambernut', '1-Milk', '2-Trigos', ''),
               ('Bread', '2-Buttler', '2-Trigos', '', '')]

class Table:

    def __init__(self, f1):

        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(f1, width=15, fg='#091174',bg='#c4c8c5',
                               font=('Arial', 10, 'bold'))

                self.e.grid(row=i+2, column=j, padx=3, pady=5)
                self.e.insert(END, lst[i][j])


def food(x=''):
    x= x.strip().upper()
    if x == '' or x not in atrib:
        messagebox.showerror('ERRO','Digite um atributo válido')

    global dict, atributo, total_rows, total_columns
    atributo = x.upper()

    try:
        if atributo == "EXP":
            lista()
            total_rows = len(lst)
            total_columns = len(lst[0])
            resp = Table(f1)

        if atributo == 'ATK':
            lista()
            total_rows = len(lst)
            total_columns = len(lst[0])
            resp = Table(f1)

        if atributo == 'ABS':
            lista()
            total_rows = len(lst)
            total_columns = len(lst[0])
            resp = Table(f1)

    except:
        messagebox.showerror('ERRO', 'Atributo não reconhecido, tente novamente!')


def ajuda():
    messagebox.showinfo('Atributos', 'Os atributos atuais do app são: ABS, EXP e ATK')


f0 = tk.Frame(janela,background='#a0ded6')
f0.grid(row=0, column=0, columnspan=3,padx=10, pady=10)

texto1 = ctk.CTkLabel(f0, text='Atributo:',width=150, corner_radius=100,fg_color='black',text_color='white',
                      bg_color='#a0ded6', font=('Arial', 14, 'bold'))
texto1.grid(row=0, column=0, padx=2, pady=10)

etexto = ctk.CTkEntry(f0, width=200, corner_radius=100, bg_color='#a0ded6',font=('Arial', 14, 'bold'))
etexto.grid(row=0, column=1, padx=2, pady=10)

button = ctk.CTkButton(f0,width=150, text='Buscar', hover_color='red',  corner_radius=10, bg_color='#a0ded6',
                       command=lambda: food(etexto.get()),font=('Arial', 14, 'bold'))
button.grid(row=0, column=2, padx=2, pady=10)

button_help = ctk.CTkButton(f0, text='Help', hover_color='red',  corner_radius=10, bg_color='#a0ded6',
                            font=('Arial', 14, 'bold'), command=lambda: ajuda(), width=25, fg_color='green')
button_help.grid(row=0,column=3, padx=2, pady=10)

f1 = tk.Frame(janela)
f1.grid(row=2, column=0,columnspan=total_columns, rowspan=total_rows)


janela.mainloop()