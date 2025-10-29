# import tkinter as tk
# import random

# def compare():
#     number1=random.randint(1,50)
#     number2=random.randint(1,50)

#     label_numbers.config(text=f"{number1} i {number2}")
    
#     if number1>number2:
#         label_result.config(text=f"{number1} більше за {number2}")
#     elif number1<number2:
#         label_result.config(text=f"{number1} менше за {number2}")
#     else:
#         label_result.config(text=f"Числа рівні")
# window = tk.Tk()
# window.title("Більше чи менше")
# window.geometry("600x400")
# label1=tk.Label(window,text="Порівння чисел",font=("Arial",18))
# label1.pack(pady=20)
# button = tk.Button(window,text="Генерувати числа",command =compare ,bg = "lightblue",font=("Arial",18))
# button.pack(pady=10)
# label_numbers = tk.Label(window,text="",font=("Arial",16))
# label_numbers.pack(pady=10)
# label_result = tk.Label(window,text="",font=("Arial",14))
# label_result.pack(pady=20)
# def pp():
#     a = entry.get()
#     label2.config(text=f"{a}")
# entry=tk.Entry(window,width=30)
# entry.pack()
# button2=tk.Button(window,text="Зняти текст",command=pp,bg="lightgreen",font=("Arial",18))
# button2.pack(pady=10)
# label2 = tk.Label(window,text="")
# label2.pack(pady=20)
# window.mainloop()
# import tkinter as tk
# window = tk.Tk()
# window.title("Введіть пароль")
# window.geometry("600x400")
# def pp():
#     a = entry.get()
#     if a == "Topparol":
#         label2.config(text=f"Пароль вірний")
#         window.configure(bg="green")
#     else:
#         label2.config(text=f"Вхід заборонено")
#         window.configure(bg="red")
    
# entry=tk.Entry(window,width=30)
# entry.pack(pady = 50)
# button2=tk.Button(window,text="Перевірити пароль",command=pp,bg="lightgreen",font=("Arial",18))
# button2.pack(pady=10)
# label2 = tk.Label(window,text="")
# label2.pack(pady=20)
# window.mainloop()
import tkinter as tk
window = tk.Tk()
window.title("Введіть пароль")
window.geometry("600x400")
def pp():
    a =int( entry.get())
    if a  %2==0:
        label2.config(text=f"парне")
        window.configure(bg="green")
    else:
        label2.config(text=f"не парне")
        window.configure(bg="red")
    
entry=tk.Entry(window,width=30)
entry.pack(pady = 50)
button2=tk.Button(window,text="перевір чи парне число",command=pp,bg="lightgreen",font=("Arial",18))
button2.pack(pady=10)
label2 = tk.Label(window,text="")
label2.pack(pady=20)
window.mainloop()