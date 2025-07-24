from tkinter import *
from tkinter import simpledialog as sd #куда будем вводить часы
from tkinter import messagebox as mb #сообщать об ошибках
import datetime
import pygame #работа со звуком
import time

t = 0
music =  False

#делаем функцию на кнопку сет, чтобы нажималась и устанавливалось напоминание
def set(): #установка напомиания
    global t
    rem = sd.askstring("Время напоминания", "введите время напоминания в формате ЧЧ:ММ в 24 часовом формате")#asc....это просто запрос текстовой строки
    #теперь получаем точное  время сейчас и изменим часы и минуты
    if rem:
        try:
            hour = int(rem.split(":")[0]) #сплит разделит на два числа часы и минуты
            minute = int(rem.split(":")[1])
            now = datetime.datetime.now() #текущее время
            print(now)
            #теперь устанавливаем то время, но которое нужно напоминание
            dt = now.replace(hour=hour, minute=minute, second=0) #меняем часы и минуты которые нужны
            print(dt)
            t = dt.timestamp() #временная метка в миллиардах секунды
            print(t)
            # добавить текст напоминания, что нам нужно сделать в это время
            text = sd.askstring("Текст напоминани", "Введите текст напоминания")
            label.config(text = f'Напоминание на {hour:02}:{minute:02} с тектсом {text}')
        except Exception as e:
            mb.showerror("Ошибка!", f' Произошла ошибка {e}')


#устанавливаем функцию , которая будет проверять наше время CHECK
def check():
    global t
    if t:
        now = time.time() #текущая временная метка
        if now >= t:
            play_snd()
            t = 0
    window.after(10000, check) #вызываем черет 10 000 милисекунд включать звук, проверку выполняет 6 раз в минуту


#Функция включения музыки
def play_snd():
    global music
    music = True
    pygame.mixer.init()
    pygame.mixer.music.load("reminder.mp3")#загружаем музыку
    pygame.mixer.music.play() #включили музыку

#Функция выключения музыки
def stop_music():
    global music #если музыка играет то знае тру, если нет то фолс
    if music:
        pygame.mixer.music.stop()
        music = False
    label.config(text = 'Установить новое анпоминание')



window=Tk()
window.title("Напоминание")
label = Label(text = 'Установить напоминание', font= ('Arial', 20))
label.pack(pady=18) #отсутуп по вертикали

set_button = Button(text = 'Установить напоминаение',command=set) #set команда установки
set_button.pack(pady=10)

stop_button = Button(text = 'Остановить музыку', command = stop_music)#кнопка отключения музыки
stop_button.pack(pady=10)
check() #запустить музыку


window.mainloop()