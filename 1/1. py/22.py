import tkinter as tk
import random
from tkinter import ttk #ткінтер стильовий )
word = ["Яблуко","Груша","Книга","Кружка","Шкаф"]
secret=random.choice(word)
def check():
    user = entry.get()
    if user == secret:
        label2.config(text="Правильно!!!!!",foreground="green")
        button1.config(state="disabled")
        entry.config(state="disabled")
    else:
        label2.config(text="НеПравильно!!!!!",foreground="red")
        entry.delete(0,"end")
    
window = tk.Tk()
window.title("Вгадай слово")
window.geometry("500x300")
label1= ttk.Label(window,text="Я загадав слово, спробуй його відгадати",font=("Arial",12)).pack(pady=20)
entry = ttk.Entry(window,font=("Arial",14),justify="center") #розмістити по горизонталі в центрі
entry.pack(pady=10)
button1=ttk.Button(window,text="Перевірити",command = check)
button1.pack(pady=10)
label2 = ttk.Label(window,text="",font=("Arial",14,"bold")) # bold - жирний шрифт
label2.pack(pady=10)
window.mainloop()
# Задача, створити програму яка при нажиманні на кнопку перевертає текст, який був введений в entry
# Задача, створити програму яка при нажиманні на кнопку перевертає текст, який був введений в entry
import ttkbootstrap as ttk
import random
from ttkbootstrap.constants import *
window = ttk.Window(themename="minty")
# Задача, створити програму яка при нажиманні на кнопку перевертає текст, який був введений в entry
