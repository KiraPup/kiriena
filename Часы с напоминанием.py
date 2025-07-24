from tkinter import *
from tkinter import simpledialog as sd #куда будем вводить часы
from tkinter import messagebox as mb #сообщать об ошибках
import datetime
import pygame #работа со звуком
import time


#делаем функцию на кнопку сет, чтобы нажималась и устанавливалось напоминание
def set(): #установка напомиания
    rem = sd.askstring("Время напоминания", "введите время напоминания в формате ЧЧ:ММ в 24 часовом формате")#asc....это просто запрос текстовой строки
    #теперь получаем точное  время сейчас и изменим часы и минуты
    if rem:
        try:
            hour = int(rem.split(":")[0]) #сплит разделит на два числа часы и минуты
            minute = int(rem.split(":")[1])
            now = datetime.now() #текущее время
            print(now)
            #теперь устанавливаем то время, но которое нужно напоминание
            dt = now.replace(hour=hour, minute=minute) #меняем часы и минуты которые нужны
            print(dt)
            t = dt.timestamp() #временная метка в миллиардах секунды
            print(t)
        except Exception as e:
            mb.showerror("Ошибка!", f' Произошла ошибка {e}')


window=Tk()
window.title("Напоминание")
label = Label(text = 'Установить напоминание')
label.pack(pady=10) #отсутуп по вертикали
set_button = Button(text = 'Установить напоминаение',command=set) #set команда установки
set_button.pack()

window.mainloop()