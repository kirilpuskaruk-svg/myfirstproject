# Домашнє завдання: кожен з вас придумує якусь гру, яку можна реалізувати в ткінтері , чекаю від вас креативу і класних програм 😊
import tkinter as tk
import random
from tkinter import ttk

words = ["компютер", "шоколадка", "клавіатура", "вентилятор", "мишка",
         "стіл", "стільчик", "подушка", "бутилка", "кульок"]
secret = random.choice(words)

attempts = 5  # кількість спроб

def check():
    global attempts
    user = entry.get()
    if user == secret:
        label2.config(text="Правильно!!!!!", foreground="green")
        button1.config(state="disabled")
        entry.config(state="disabled")
    else:
        attempts -= 1
        if attempts == 0:
            label2.config(text=f"Спроби закінчились! Було слово: {secret}", foreground="red")
            button1.config(state="disabled")
            entry.config(state="disabled")
        else:
            label2.config(text=f"Неправильно! Залишилось {attempts}", foreground="red")
        entry.delete(0, "end")

window = tk.Tk()
window.title("Вгадай слово")
window.geometry("500x300")

ttk.Label(window, text="Я загадав слово, спробуй його відгадати", font=("Arial", 12)).pack(pady=20)

entry = ttk.Entry(window, font=("Arial", 14), justify="center")
entry.pack(pady=10)

button1 = ttk.Button(window, text="Перевірити", command=check)
button1.pack(pady=10)

label2 = ttk.Label(window, text="", font=("Arial", 14, "bold"))
label2.pack(pady=10)

window.mainloop()