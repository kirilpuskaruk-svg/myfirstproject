# import random

# # Список локацій
# places = ["Старий млин", "Забутий колодязь", "Печера дракона",
#           "Скеля самотності", "Водоспад", "Темний ліс", "Зруйнований замок"]

# # Випадково вибираємо, де буде скарб
# treasure_location = random.choice(places)

# print("Ласкаво просимо у гру-квест! 🎮")
# print("Твоя мета – знайти скарб! 🏆")

# attempts = 0  #

# while True:
#     attempts += 1
    
#     # Випадково вибираємо локацію
#     current_location = random.choice(places)
    
#     # Якщо знайдений скарб
#     if current_location == treasure_location:
#         print(f"🎉 Вітаю! Ти знайшов скарб у локації")
#         print(f"Тобі знадобилося спроб(и).")
#         break
#     else:
#         print(f"Ти прибув до  Скарбу тут немає. Спробуй ще раз.")
    
#     # Запит, чи продовжити
#     answer = input("Продовжити пошуки? (так/ні): ").lower()
#     if answer != "так":
#         print("\nГра закінчена. Скарб залишився нерозгаданим...")
#         print(f"Тобі знадобилося  спроб.")
#         break
from ursina import * 
import random 
app = Ursina()
gravets = Entity(model="cube",color=color.red,position=(0,0,0),scale=(1,1,1))
gravets2=Entity(model="cube",color=color.yellow,position=(-1,3,2),scale=(1,1,1))
gravets3=Entity(model="cube",color=color.orange,position=(-3,4,4),scale=(1,1,1))
monetka = Entity(model="sphere",color=color.orange,position=(1,0,0),scale=(0.5,0.5,0.5))
ochky = 0
tekst_ochok = Text(text=f"очки {ochky}",position=(-0.85,0.45),scale=2)
def update():
    speed = 5
    if held_keys["shift"]:
        speed=10
    if held_keys["w"]:
        gravets.z+=speed*time.dt
    if held_keys["s"]:
        gravets.z-=speed*time.dt
    if held_keys["d"]:
        gravets.x+=speed*time.dt
    if held_keys["a"]:
        gravets.x-=speed*time.dt
    if held_keys["up arrow"]:
        gravets.y+=speed*time.dt
    if held_keys["down arrow"]:
        gravets.y-=speed*time.dt
    vidstan = distance(gravets.position,monetka.position)
    if vidstan<1:
        collect()
def collect():
    global ochky
    ochky+=1
    monetka.position = (random.randint(-4,4),random.randint(-4,4),random.randint(-4,4))
    tekst_ochok.text = f"очки {ochky}"
camera.position = (0, 15, -15)
camera.rotation_x=45
app.run()