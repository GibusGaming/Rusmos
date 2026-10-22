import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from tkinter.ttk import *
from math import *
from grafics import *
from count_sys import *
from calc import calc_slv
from dif_int import *

def grafik():
    def grf():
        exp = txt.get()
        cnt = int(count.get())
        lbl.config(text = graf(exp,cnt))
    window = Tk()
    window.title("Графики")
    window.geometry("350x200")

    Label(
        window,
        text="Функция (используйте x):"
    ).grid(column=0, row=0)

    txt = Entry(window, width=20)
    txt.grid(column=1, row=0)

    Label(
        window,
        text="Диапазон X:"
    ).grid(column=0, row=1)

    count = Entry(window, width=10)
    count.grid(column=1, row=1)

    lbl = Label(window, text="")
    lbl.grid(column=0, row=2, columnspan=2)

    Button(
        window,
        text="Построить график",
        command=grf
    ).grid(column=0, row=3)

    Button(
        window,
        text="Закрыть",
        command=window.destroy
    ).grid(column=1, row=3)

    window.mainloop()

def count_system():
    def convert_number():
        result = coconut(entry_number.get(),int(entry_from_base.get()),int(entry_to_base.get()))
        label_result.config(text=f"Результат: {result}")
    tk=Tk()
    tk.title("Перевод систем счисления")
    label = Label(tk)
    label_number = Label(tk, text="Введите число:")
    label_number.grid(row=0, column=0, padx=10, pady=10)
    entry_number = Entry(tk)
    entry_number.grid(row=0, column=1, padx=10, pady=10)
    label_from_base = Label(tk, text="Из системы счисления (2-36):")
    label_from_base.grid(row=1, column=0, padx=10, pady=10)
    entry_from_base = Entry(tk)
    entry_from_base.grid(row=1, column=1, padx=10, pady=10)
    label_to_base = Label(tk, text="В систему счисления (2-36):")
    label_to_base.grid(row=2, column=0, padx=10, pady=10)
    entry_to_base = Entry(tk)
    entry_to_base.grid(row=2, column=1, padx=10, pady=10)
    button_convert = Button(tk, text="Перевести", command=convert_number)
    button_convert.grid(row=3, column=0, columnspan=2, pady=10)
    label_result = Label(tk, text="Результат:")
    label_result.grid(row=4, column=0, columnspan=2, pady=10)
    tk.mainloop()

def calc():
    def calc_solver():
        s = txt.get()
        lbl.configure(text=calc_slv(s)) 
    calc=Tk()
    calc.geometry('605x200')
    txt = Entry(calc,width=100)
    txt.grid(column=3, row=0)
    lbl=Label(calc, text="результат:")
    lbl.grid(column=3, row=1)
    btn=Button(calc, text="расчитать", command=calc_solver)
    btn.grid(column=3, row=2)
    calc.mainloop()

def in_dif():
    def yaf():
        ex = expr.get()
        typ = cmb.get()
        lbl.config(text=prints(ex,typ))
    tk = Tk()
    tk.title('Матан')
    tk.geometry('500x500')
    expr = Entry(tk)
    expr.grid(column=0,row=0)
    cmb = Combobox(tk,values = ['Производная','Интеграл'])
    cmb.grid(column = 1,row = 0)
    btn = Button(tk,text='Вычислить',command=yaf)
    lbl=Label(tk,text='Результат ')
    btn.grid(column=0,row=1)
    lbl.grid(column=0,row=2)
    tk.mainloop()

root=Tk()
root.title("Вообще лучший калькулятор mk.6.66")
root.geometry('500x500')
grf=Button(root,text='Графики функций', command=grafik)
grf.grid(column=0,row=0)
base=Button(root,text='Системы счисления', command=count_system)
base.grid(column=0,row=1)
calculator=Button(root,text='Калькулятор', command=calc)
calculator.grid(column=1,row=0)
prin = Button(root,text='Дифференцирование',command=in_dif)
prin.grid(column=1,row=1)
root.mainloop()
