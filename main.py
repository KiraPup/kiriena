from tkinter import *
from tkinter import ttk # виджеты
import calculator_logic as c

oper = ("")
first = 0
second = 0
result = 0


#Функция для запуска работы калькулятора
def calc():

    global result
    try:
        if oper == 'x²':
            result = c.square(first)
        else:
            second = float(entry.get())
            if oper == '+': #переменная опер это операция , мы ее создали вверху
                    result = c.add(first, second) # если сложение значит результат функции сложения, указываем два параметра, так
        #как в функции у нас а и б , мы их называем первый и второй эти значения будем вводить, с помощью entry
            elif oper == '-':
                    result = c.subtract(first, second)
            elif oper == '*':
                    result = c.multiply(first, second)
            elif oper == '/':
                    result = c.divide(first, second)



        entry.delete(0, END)#удалили после второго слагаемого поле ввода
        entry.insert(0, str(result))#записываем результат в поле ввода, стр это то что превращает в текст
    except ValueError:
          entry.delete(0, END)  # удалили после второго слагаемого поле ввода
          entry.insert(0, 'Ошибка результата')

#Функция ввода числа
def enter_number(number):
    entry.insert(END, number) #вводить число


#очистка поля
def clear_entry():
    entry.delete(0, END)


#Функция при нажатии на кнопку +, -, *, / падала правильна функция
def set_operation(operation):
    global  first #Мы их ввели за пределами функции, чтобы их использовтаь нужно так написать
    global oper
    try:
          first = float(entry.get())  # превратим в число и положим в перемнную ферст
          oper = operation
          if oper =='x²':
              calc()
          else:
              entry.delete(0, END)
    except ValueError:
          entry.delete(0, END)  # очистили поле ввода


def validate_entry():
    e = entry.get() #прочитали переменную
    txt = ''.join(b for b in e if b in '0123456789.-')#склеит элементы списков в скобках
#для каждого б в списке е, для каждого е в списке б из разрешенного списка в скобках
    if e != txt:
        entry.delete(0, END)#удаляем не разрешенные символы
        entry.insert(0, txt) #оставляем только разрешенные символы



window= Tk()
window .title("Калькулятор")

entry = ttk.Entry(width=20) #табло
entry.grid(row=0, column=0, columnspa=4, sticky='ew')

#Отладка , чтобы не могли вводить какую тоо ерунду
entry.bind('<KeyRelease>', lambda event: validate_entry())

ttk.Button(text='1', command=lambda:enter_number('1')).grid(row=1,column=0)
ttk.Button(text='2', command=lambda:enter_number('2')).grid(row=1,column=1)
ttk.Button(text='3', command=lambda:enter_number('3')).grid(row=1,column=2)
ttk.Button(text='4', command=lambda:enter_number('4')).grid(row=2,column=0)
ttk.Button(text='5', command=lambda:enter_number('5')).grid(row=2,column=1)
ttk.Button(text='6', command=lambda:enter_number('6')).grid(row=2,column=2)
ttk.Button(text='7', command=lambda:enter_number('7')).grid(row=3,column=0)
ttk.Button(text='8', command=lambda:enter_number('8')).grid(row=3,column=1)
ttk.Button(text='9', command=lambda:enter_number('9')).grid(row=3,column=2)
ttk.Button(text='0', command=lambda:enter_number('0')).grid(row=4,column=0)

ttk.Button(text='C', command=clear_entry).grid(row=4,column=1)
ttk.Button(text='=', command=calc).grid(row=4,column=2)

ttk.Button(text ='x²', command=lambda:set_operation('x²')).grid(row=5,column=0, sticky='nsew')

#Арифметические операции
ttk.Button(text='+', command=lambda:set_operation('+')).grid(row=1,column=3)
ttk.Button(text='-', command=lambda:set_operation('-')).grid(row=2,column=3)
ttk.Button(text='*', command=lambda:set_operation('*')).grid(row=3,column=3)
ttk.Button(text='/', command=lambda:set_operation('/')).grid(row=4,column=3)




window.mainloop()