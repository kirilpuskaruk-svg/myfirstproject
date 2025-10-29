# Turtle 
# Turtle Graphics - бібліотека для малювання різної графіки за допомогою черепашок

#import turtle 

# # Створення екрану
# s = turtle.getscreen()
# #Створення черепашки
# t = turtle.Turtle()
# # Скриття черепашки
# t.hideturtle()
# # Завершення програми
# turtle.done()
# # рух черепахи
# t.forward(100) #рух вперед на 100 пікселів
# t.backward(100) #рух назад на 100 пікселів
# t.left(90) #поворот на 90 градусів
# t.right(90) #поворот на 90 градусів

# # Переміщення до точки
# t.goto(100, 100) # переміщення до точки (100, 100)
# t.home() # повернення до початкової точки
# Малювання квадрату
# import turtle

#t = turtle.Turtle()
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)

# turtle.done()

# Керування пером (пензликом)

#t.penup() # підняти перо
# t.pendown() # опустити перо

# t.pensize(10) # змінити товщину пера
# t.pencolor("red") # змінити колір пера
# t.speed(5) # змінити швидкість черепахи 0 - найвища швидкість

# # готові фігури
# t.circle(50) # малює коло радіусом 50 пікселів
# t.dot(20) # точку з діаметром 20 пікселів
# t.speed(1)
# t.fillcolor("blue") # змінити колір заповнення
# t.begin_fill() # початок заповнення
# t.circle(50) # малює коло радіусом 50 пікселів
# t.end_fill() # кінець заповнення
# turtle.done()

# задача намалювати трикутник з заливкою зеленою

# import turtle

# t=turtle.Turtle()
# t.fillcolor("green")
# t.begin_fill()
# # малювання папємаше
# # for i in range(5):
# #     t.forward(100)
# #     t.left(90)
# # t.goto(100,100)
# # for i in range(5):
# #     t.forward(100)
# #     t.left(90)
# # t.goto(200,100)
# # for i in range(5):
# #     t.forward(100)
# #     t.left(90)
# # t.goto(300,200)
# # for i in range(5):
# #     t.forward(100)
# #     t.left(90)
# # t.end_fill()
# # малювання папємаше
# n=10
# while n<=50:
#     t.circle(n)
#     n+=10
# turtle.done()

# налаштування екрану 
# turtle.bgcolor("black") # колір фону
# turtle.title("Моя програма") # назва екрану

# t=turtle.Turtle()
# t.shape("turtle") # форма черепашки
# t.color ("red","green") # колір черепашки, колір заповнення
# t.shapesize(2,2,2) # розмір черепашки

# додаткові команди
# t.clear() # очищує екран
# t.reset() # скидує налаштування
# t.undo() # скасовує останню дію
# t.stamp() # залишає відбиток черепахи

# # отримання інформації
# t.position() # повертає поточну позицію
# t.heading() # повертає поточний напрямок
# t.isdown() # повертає чи піднятий перо # True or False

# Різнокольорві кола
# Намалюйте 5 кіл різних кольорів розташованих по колу

# import turtle 
# colors = ["red", "green", "blue", "yellow", "purple"]
# t=turtle.Turtle()
# t.shape("turtle")
# t.color("black", "white")
# t.shapesize(2,2,2)
# t.pensize(10)
# t.speed(3)
# for i in range(5):
#     t.pencolor(colors[i])
#     t.circle(30)
#     t.penup()
#     t.forward(70)
#     t.pendown()
#     t.right(72)
# turtle.done()
# Намалюйте зірку п'ятикутну
# import turtle
# t=turtle.Turtle()
# t.right(144)
# for i in range(5):
#     t.forward(10)
#     t.left(90)
# t.goto(100,100)
# for i in range(5):
#     t.forward(4000)
#     t.left(90)
# t.goto(200,100)
# for i in range(5):
#     t.forward(2000)
#     t.left(90)
# t.goto(300,200)
# for i in range(5):
#     t.forward(1000)
#     t.left(90)
# t.end_fill()
# turtle.done()
# Завдання 3: Смайлик
# Складається з елементів:
# Жовте обличчя - велике коло
# Очі - два маленькі чорні кола
# Ніс - маленький трикутник
# Усмішка - дуга (частина кола)
# Рум'янець - рожеві кола на щоках
# Брови - прямі лінії для виразності

# import turtle 

# t = turtle.Turtle()
# t.speed(8)
# screen = turtle.Screen()
# screen.bgcolor("white")
# screen.title("Смайлик")

# def move_to(x, y):
#     t.penup()
#     t.goto(x, y)
#     t.pendown()

# def draw_filled_circle(radius, color, fill_color):
#     t.color(color)
#     t.fillcolor(fill_color)
#     t.begin_fill()
#     t.circle(radius)
#     t.end_fill()
# Завдання 2: Сім'я геометричних фігур
# Малюнок включає 6 різних фігур:
# Квадрат (4 сторони, поворот 90°)
# Трикутник (3 сторони, поворот 120°)
# Коло (функція circle())
# Шестикутник (6 сторін, поворот 60°)
# Зірка (5 променів, поворот 144°)
# Восьмикутник (8 сторін, поворот 45°)
# Кожна фігура має свій колір та розташування на екрані.
import turtle
t= turtle.Turtle()
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)

turtle.done()





