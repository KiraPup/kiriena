from tkinter import *
from tkinter import simpledialog as sd #куда будем вводить часы
from tkinter import messagebox as mb #сообщать об ошибках
import datetime
import pygame #работа со звуком
import time

t = None

music = False  # Переменная для отслеживания проигрывания музыки


def set():
    global t
    rem = sd.askstring("Время напоминания", "Введите время в формате ЧЧ:ММ (24-часовой формат)")
    if rem:
        try:
            par = rem.split(':')
            if len(par) != 2:
                mb.showerror("Ошибка","Неверный формат времени")
            hour = int(rem.split(":")[0])
            minute = int(rem.split(":")[1])
            if hour < 0 or hour > 23:
                mb.showerror("Ошибка", "часы должны быть от 00 до 23")
            if minute <0 or minute > 59:
                mb.showerror("Ошибка","Минуты должны быть от 00 до 59")
            now = datetime.datetime.now()
            dt = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
            t = dt.timestamp()
            label.config(text=f"Напоминание установлено на: {hour:02}:{minute:02}")

        except ValueError:
            mb.showerror("Ошибка", "Неверный формат времени")


def check():
    global t
    if t:
        now = time.time()
        if now >= t:
            play_snd()
            t = None
    window.after(10000, check)


def play_snd():
    global music
    music = True
    pygame.mixer.init()
    pygame.mixer.music.load("reminder.mp3")
    pygame.mixer.music.play()


def stop_music():
    global music
    if music:
        pygame.mixer.music.stop()
        music = False
    label.config(text="Установить новое напоминание")


window = Tk()
window.title("Напоминание")

label = Label(text="Установите напоминание", font=("Arial", 14))
label.pack(pady=10)

set_button = Button(text="Установить напоминание", command=set)
set_button.pack(pady=10)

stop_button = Button(text="Остановить музыку", command=stop_music)
stop_button.pack(pady=5)

check()

window.mainloop()