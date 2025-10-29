# Умовний оператор
# if умова:
#     блок коду
#     будь який код
#     будь якої величини
#     будь якої довжини
#     і поки він з відступом 
#     він належить до ось цього if

# elif умова:
#     блок коду
#     будь який код
#     будь якої величини
#     будь якої довжини
#     і поки він з відступом 
#     він належить до ось цього elif
# else: # без умови бо це будь яка інша або непердбачувана або зазвичай неправильна 
#     #коли не задовільнинилсь всі інші умови переходим до крайньої
#     помилка
#     або якась дія яку ми зробимо в будь якому випадку

# a = int(input("Напишіть будь яке число "))
# if a>0:
#     print("Додатнє число")
# elif a<0:
#     print("Від'ємне число")
# #Ця умова
# elif a==0:
#     print("Нуль")
# #І ця умова
# # else:
# #     print("Нуль")
# while True:
#     a = int(input("Напишіть будь яке число "))
#     if a>=0:
#         print("Додатнє число")
#     else:
#         print("Від'ємне")

# Функції
# print()
# input()
# import random
# random.randint()
# random.choice()

#Створення фукції 
# def назва функції (список аргументів):
#     блок коду, який буде виконуватись при виклику функції

# def sayhelloprivetandpaka():
#     print("Hello privet paka ")

# def spk():
#     print("Hello privet paka ")
# spk()

#Позиційні аргументи і функції з аргументами 

# def peremnozhnasebe(x):
#     print(x*x)
# peremnozhnasebe(100)
# peremnozhnasebe(2)
# peremnozhnasebe(4)
# peremnozhnasebe(8)
# peremnozhnasebe(10)
# peremnozhnasebe(50)

# Створити функцію яка перемножує A B C 
# def kruto(a,b,c):
#     print(a*b*c)
#     print(f"a= {a} ")
#     print(f"b= {b} ")
#     print(f"c= {c} ")

# kruto(4,10,20)


# def opus(name,city,age):
#     print(f"Мене звати {name},я живу в {city} і мені {age} років")
# opus("Sasha","Kyiv","22")
# opus("Nikopole","11","Dima")
# opus(city="Nikopole",age="11",name="Dima")
# opus("Dima",age="11",city="Nikopole") # ось так робити можна
# opus(age="11","Dima",city="Nikopole") #SyntaxError: positional argument follows keyword argument
# #Якщо використовуєте змішаний то тоді позиційні аргументи завжди мають бути на першому місці 
# def opus(name,city,age,country="Ukraine"):
#     print(f"Мене звати {name},я живу в {city} {country} і мені {age} років")
# opus("Sasha","Kyiv","22")
# opus("Kirill","Paris","12","France")


# def calculate(a,b):
#     resultat = a+b
#     return resultat
# print(calculate(10,20))
# def calculate2(a,b):
#     print(a+b+calculate(a,b))
# calculate2(10,20)

# x = 10
# def plusx():
#     global x
#     x+=5
#     print(x)
# plusx()
# print(x)
# 12. Вводяться два цілих числа. Визначити, чи діляться вони націло одне на одне.
# Якщо діляться, то вивести результат їхнього ділення
# a=int(input())
# b=int(input())
# if a % b==0:
#     print(a//b)
# 1. Дано два цілих числа. Виведіть значення найменшого з них.
# Авто-клікер (Windows). В коді немає ключового слова `import` — модулі підвантажуються через __import__.
import threading
import time
import tkinter as tk
from tkinter import ttk
import pyautogui

class AutoClicker:
    def __init__(self):
        self.running = False
        self.delay = 0.1  # затримка між кліками (секунди)
        self.button = 'left'  # кнопка миші (left / right / middle)

    def start(self):
        if not self.running:
            self.running = True
            threading.Thread(target=self.run, daemon=True).start()

    def stop(self):
        self.running = False

    def run(self):
        while self.running:
            pyautogui.click(button=self.button)
            time.sleep(self.delay)

class App:
    def __init__(self, root):
        self.root = root
        root.title("Game AutoClicker")
        root.geometry("250x200")

        self.clicker = AutoClicker()

        # Інтервал
        ttk.Label(root, text="Інтервал (сек):").pack(pady=5)
        self.delay_var = tk.DoubleVar(value=0.1)
        ttk.Entry(root, textvariable=self.delay_var).pack(pady=5)

        # Вибір кнопки миші
        ttk.Label(root, text="Кнопка миші:").pack(pady=5)
        self.button_var = tk.StringVar(value="left")
        ttk.Combobox(root, textvariable=self.button_var,
                     values=["left", "right", "middle"]).pack(pady=5)

        # Кнопки управління
        ttk.Button(root, text="Start", command=self.start_clicker).pack(pady=10)
        ttk.Button(root, text="Stop", command=self.stop_clicker).pack(pady=5)

    def start_clicker(self):
        try:
            self.clicker.delay = float(self.delay_var.get())
        except:
            self.clicker.delay = 0.1
        self.clicker.button = self.button_var.get()
        self.clicker.start()

    def stop_clicker(self):
        self.clicker.stop()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
