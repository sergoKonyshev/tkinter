from tkinter import *
import math
root = Tk()
root.title('Калькулятор')

ent = Entry(root, width = 26, justify='right', bd=10, insertwidth=-0.5)
ent.grid(row = 0, columnspan = 5, padx = 5, pady = 5)

def number_button(num):
    ent.insert(END, str(num))

def clear():
    ent.delete(0, END)

def clear2():
    n = ent.get()
    ent.delete(len(n)-1)

def sqrt():
    s = ent.get()
    try:
        s = int(s)
        f = math.sqrt(s)
        clear()
        ent.insert(0, f)
    except Exception:
        clear()
        ent.insert(0, 'Error!')

def factorial():
    s = ent.get()
    try:
        s = int(s)
        f = 1
        for i in range(1, s+1):
            f *= i
        clear()
        ent.insert(0, f)
    except Exception:
        clear()
        ent.insert(0, 'Error!')

def equal():
    s = ent.get()
    try:
        result = eval(s)
        clear()
        ent.insert(0, result)
    except Exception:
        clear()
        ent.insert(0, 'Error!')

btn_01 = Button(root, text = 'n!', width = 3, height = 1, command = factorial)
btn_01.grid(row = 2, column = 0, padx = 5, pady = 5)
btn_ce = Button(root, text = 'CE', width = 3, height = 1, command = clear)
btn_ce.grid(row = 2, column = 1, pady = 5)
btn_c = Button(root, text = 'C', width = 3, height = 1, command = clear2)
btn_c.grid(row = 2, column = 2, padx = 5, pady = 5)
btn_sqrt = Button(root, text = 'sqrt', width = 3, height = 1, command = sqrt)
btn_sqrt.grid(row = 2, column = 3, pady = 5)
btn_sqr = Button(root, text = '^', width = 3, height = 1, command = lambda: number_button('**'))
btn_sqr.grid(row = 2, column = 4, padx = 5, pady = 5)

btn_7 = Button(root, text = '7', width = 3, height = 1, command = lambda: number_button('7'))
btn_7.grid(row = 3, column = 0, padx = 5)
btn_8 = Button(root, text = '8', width = 3, height = 1, command = lambda: number_button('8'))
btn_8.grid(row = 3, column = 1)
btn_9 = Button(root, text = '9', width = 3, height = 1, command = lambda: number_button('9'))
btn_9.grid(row = 3, column = 2, padx = 5)
btn_03 = Button(root, text = '/', width = 3, height = 1, command = lambda: number_button('/'))
btn_03.grid(row = 3, column = 3)
btn_per = Button(root, text = '(', width = 3, height = 1, command = lambda: number_button('('))
btn_per.grid(row = 3, column = 4, padx = 5)

btn_4 = Button(root, text = '4', width = 3, height = 1, command = lambda: number_button('4'))
btn_4.grid(row = 4, column = 0, padx = 5, pady = 5)
btn_5 = Button(root, text = '5', width = 3, height = 1, command = lambda: number_button('5'))
btn_5.grid(row = 4, column = 1, pady = 5)
btn_6 = Button(root, text = '6', width = 3, height = 1, command = lambda: number_button('6'))
btn_6.grid(row = 4, column = 2, padx = 5, pady = 5)
btn_04 = Button(root, text = '*', width = 3, height = 1, command = lambda: number_button('*'))
btn_04.grid(row = 4, column = 3, pady = 5)
btn_05 = Button(root, text = ')', width = 3, height = 1, command = lambda: number_button(')'))
btn_05.grid(row = 4, column = 4, padx = 5)

btn_1 = Button(root, text = '1', width = 3, height = 1, command = lambda: number_button('1'))
btn_1.grid(row = 5, column = 0, padx = 5)
btn_2 = Button(root, text = '2', width = 3, height = 1, command = lambda: number_button('2'))
btn_2.grid(row = 5, column = 1)
btn_3 = Button(root, text = '3', width = 3, height = 1, command = lambda: number_button('3'))
btn_3.grid(row = 5, column = 2, padx = 5)
btn_06 = Button(root, text = '-', width = 3, height = 1, command = lambda: number_button('-'))
btn_06.grid(row = 5, column = 3)
btn_07 = Button(root, text = '=', width = 3, height = 3, command = equal)
btn_07.grid(rowspan = 2, row = 5, column = 4, padx = 5, pady = 5)

btn_0 = Button(root, text = '0', width = 8, height = 1, command = lambda: number_button('0'))
btn_0.grid(row = 6, column = 0, columnspan = 2, padx = 5, pady = 5)
btn_08 = Button(root, text = ',', width = 3, height = 1, command = lambda: number_button('.'))
btn_08.grid(row = 6, column = 2, pady = 5)
btn_09 = Button(root, text = '+', width = 3, height = 1, command = lambda: number_button('+'))
btn_09.grid(row = 6, column = 3, pady = 5)

