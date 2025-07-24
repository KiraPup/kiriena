from tkinter import *
from tkinter import simpledialog as sd #куда будем вводить часы
from tkinter import messagebox as mb #сообщать об ошибках
import datetime
import pygame #работа со звуком
import time

window=Tk()
window.title("Напоминание")
label = Label(text = 'Установить напоминание')
label.pack(pady=10) #отсутуп по вертикали
set_button = Button(text = 'Установить напоминаение',command=set) #set команда установки
set_button.pack()

window.mainloop()