# import tkinter as tk
# window = tk.Tk() # створити вікно програми
# window.title("Перша програма ") # назва програми
# window.geometry("600x500") # розмір вікна  (ширинаxвисота)
# window.resizable(True,True) # дозволити чи заборонити змінювати розмір вікна 

# def onclick():
#     label1.config(text="Кнопка була натиснута") # .config(text) дозволя редагувати і писати новий текст
# #Створюємо напис
# label1 = tk.Label(window,text="Привіт це моя супер програма ",font=("Arial",20)) #створення надпису (вікно,текст,шрифт(шрифт не обов'язково))
# label1.pack(pady=50) # pady - відступ в даному випадку 50 пікселів, можна його не писати

# #Кнопка
# button1 = tk.Button(window,text="Кляцни мене",command = onclick , bg="lightblue",font=("Arial",20)) # (вікно,текст,функція яка активовується при нажатті кнопки,задній фон bg (не обов'язково),шрифт(шрифт не обов'язково))
# button1.pack(pady=100)
# window.mainloop()

# import tkinter as tk

# count = 0

# def plus():
#     global count
#     count+=1
#     label1.config(text=f"Рахунок {count}")
# def minus():
#     global count
#     count-=1
#     label1.config(text=f"Рахунок {count}")
# def reset():
#     global count
#     count=0
#     label1.config(text=f"Рахунок {count}")

# window = tk.Tk()
# window.title("Лічильник")
# window.geometry("300x200")

# label1 = tk.Label(window,text="Рахунок: 0",font=("Arial",30))
# label1.pack(pady=20)

# buttonplus=tk.Button(window,text="+1",command=plus,bg="lightgreen",width=50,height=10,font=("Arial",20))
# buttonplus.pack(pady=5)

# buttonminus=tk.Button(window,text="-1",command=minus,bg="pink",width=50,height=10,font=("Arial",20))
# buttonminus.pack(pady=5)

# buttonreset=tk.Button(window,text="Скинути",command=reset,bg="yellow",width=50,height=10,font=("Arial",20))
# buttonreset.pack(pady=5)

# buttonexit=tk.Button(window,text="Вийти",command=window.quit,bg="red",width=50,height=10,font=("Arial",20)) #window.quit - вихід
# buttonexit.pack(pady=5)
# window.mainlo
# import tkinter as tk
# count = 0
# def plus():
#     global count
#     count+=1
#     label1.config(text=f"робукси  {count}")

# window = tk.Tk()
# window.title("робукси")
# window.geometry("300x200")
# label1 = tk.Label(window,text="робукси: 0",font=("Arial",30))
# label1.pack(pady=20)
# buttonplus=tk.Button(window,text="Кляцни мене і получиш робукси",command=plus,bg="lightgreen",width=50,height=10,font=("Arial",20))
# buttonplus.pack(pady=5)
# buttonexit=tk.Button(window,text="Вийти",command=window.quit,bg="red",width=50,height=10,font=("Arial",20)) #window.quit - вихід
# buttonexit.pack(pady=5)
# window.mainloop()
# randomizer.py
# Простий універсальний рандомайзер у Python
# Працює на Python 3.7+

# import random
# import secrets
# import string

# def rand_int(a: int, b: int) -> int:
#     """Випадкове ціле число від a до b (включно)."""
#     return random.randint(a, b)

# def rand_float(a: float, b: float) -> float:
#     """Випадкове дійсне число в інтервалі [a, b)."""
#     return random.uniform(a, b)

# def choose_from_list(items):
#     """Випадковий вибір одного елемента зі списку."""
#     if not items:
#         raise ValueError("Список порожній")
#     return random.choice(items)

# def shuffle_list(items):
#     """Повертає тасований список (не змінює оригінал)."""
#     new = items[:]
#     random.shuffle(new)
#     return new

# def weighted_choice(items, weights):
#     """Вибір із вагами. items і weights мають однакову довжину."""
#     return random.choices(items, weights=weights, k=1)[0]

# def generate_password(length=12, use_upper=True, use_digits=True, use_symbols=True):
#     """Генерує криптографічно стійкий пароль (secrets)."""
#     alphabet = string.ascii_lowercase
#     if use_upper:
#         alphabet += string.ascii_uppercase
#     if use_digits:
#         alphabet += string.digits
#     if use_symbols:
#         alphabet += "!@#$%^&*()-_=+[]{};:,.<>/?"
#     if length < 1:
#         raise ValueError("Довжина має бути >= 1")
#     # Використовуємо secrets.choice для більшої безпеки
#     return ''.join(secrets.choice(alphabet) for _ in range(length))

# def lotto_numbers(n=6, start=1, end=49, unique=True):
#     """Генерує n лотерейних чисел у діапазоні [start, end].
#        Якщо unique=True, числа не повторюються."""
#     if unique:
#         if n > (end - start + 1):
#             raise ValueError("Неможливо вибрати стільки унікальних чисел із цього діапазону")
#         return sorted(random.sample(range(start, end+1), n))
#     else:
#         return [random.randint(start, end) for _ in range(n)]

# def example_usage():
#     print("=== Приклади використання рандомайзера ===")
#     print("rand_int(1, 10):", rand_int(1, 10))
#     print("rand_float(0, 1):", rand_float(0, 1))
#     fruits = ['apple', 'banana', 'cherry']
#     print("choose_from_list:", choose_from_list(fruits))
#     print("shuffle_list:", shuffle_list(fruits))
#     items = ['a','b','c']
#     weights = [10, 1, 1]
#     print("weighted_choice (переважно 'a'):", weighted_choice(items, weights))
#     print("generate_password(16):", generate_password(16))
#     print("lotto_numbers():", lotto_numbers())

# if __name__ == "__main__":
#     # Якщо хочеш — запускай приклади, або викликай функції з іншого скрипту.
#     example_usage(
